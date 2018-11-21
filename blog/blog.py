from .safe_cursor import SafeCursorMeta

class Blog(metaclass=SafeCursorMeta):
    def blog_create(self):
        pass

    def blog_edit(self):
        pass


    def blog_delete(self):
        pass

    def blog_list(self):
        pass

    def blog_list_user(self):
        pass
