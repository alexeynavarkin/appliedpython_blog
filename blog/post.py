from .blog_tools import SafeCursorMeta


class Post(metaclass=SafeCursorMeta):
    def __init__(self, connection, blogs=None):
        # TODO: move to parent class
        self._connection = connection
        self._blogs = blogs

    def post_create(self, cursor):
        sql = ""


    def post_edit(self):
        pass


    def post_delete(self):
        pass
