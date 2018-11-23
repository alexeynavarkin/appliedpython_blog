from types import FunctionType
from functools import wraps


def safe_cursor(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        with self._connection.cursor() as cursor:
            response = method(self, *args, cursor, **kwargs)
            self._connection.commit()
            return response
    return wrapper


def require_auth(method):
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        if self._blogs._session:
            return method(self, *args, **kwargs)
        else:
            raise RuntimeError("Unauthorised.")
    return wrapper


class SafeCursorMeta(type):
    def __new__(meta, class_name, bases, class_dict):
        new_class_dict = {}
        for attribute_name, attribute in class_dict.items():
            if isinstance(attribute, FunctionType):
                if "cursor" in attribute.__code__.co_varnames[:attribute.__code__.co_argcount]:
                    attribute = safe_cursor(attribute)
            new_class_dict[attribute_name] = attribute
        return type.__new__(meta, class_name, bases, new_class_dict)