from .blog_tools import SafeCursorMeta


class Post(metaclass=SafeCursorMeta):
    def __init__(self, connection):
        self._connection = connection

    def post_create(self, cursor):
        sql = ""


    def post_edit(self):
        pass


    def post_delete(self):
        pass
