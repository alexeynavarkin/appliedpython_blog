from .blog_tools import SafeCursorMeta


class Blog(metaclass=SafeCursorMeta):
    def __init__(self, connection, blogs=None):
        # TODO: maybe move to parent class
        self._connection = connection
        self._blogs = blogs

    def check_auth(self):
        # TODO: maybe move to parent class by meta
        if not self._blogs._user:
            raise RuntimeError("Unauthorised.")

    def check_auth_blog(self, blog_id, cursor=None):
        self.check_auth()
        sql = "SELECT User_id FROM Blog WHERE id=%s"
        cursor.execute(sql, blog_id)
        if cursor.rowcount:
            blog_user = cursor.fetchone()
            if not blog_user["User_id"] == self._blogs._user["id"]:
                raise ValueError("Only owner can modify blog.")
        else:
            raise ValueError("No Blog with such name.")

    def get(self, blog_id, cursor=None):
        sql = "SELECT * FROM Blog WHERE id=%s AND NOT deleted"
        cursor.execute(sql, blog_id)
        blog = cursor.fetchone()
        return blog

    def create(self, blog_name, cursor=None):
        # TODO: probably allow duplicate blog names so allow delete only on key
        self.check_auth()
        sql = "SELECT * FROM Blog WHERE name=%s"
        cursor.execute(sql, blog_name)
        if not cursor.rowcount:
            sql = "INSERT INTO Blog (name, user_id) VALUES (%s, %s)"
            cursor.execute(sql, (blog_name, self._blogs._user["username"]))
        else:
            raise ValueError("Blog with such name already exists.")

    def edit(self, blog_id, new_blog_name, cursor=None):
        self.check_auth_blog(blog_id)
        sql = "UPDATE Blog SET name=%s WHERE id=%s"
        cursor.execute(sql,(new_blog_name, blog_id))
        if not cursor.rowcount:
            raise ValueError("No Blog with such id. Nothing renamed.")

    def delete(self, blog_id, cursor=None):
        self.check_auth_blog(blog_id)
        sql = "UPDATE Blog SET deleted=True WHERE id=%s;"
        cursor.execute(sql, blog_id)
        if not cursor.rowcount:
            raise ValueError("No Blog with such name.")

    def list(self, cursor=None):
        sql = "SELECT * FROM Blog WHERE NOT deleted"
        cursor.execute(sql)
        return cursor.fetchall()

    def list_user(self, cursor=None):
        self.check_auth()
        sql = "SELECT * FROM Blog WHERE User_id=%s AND NOT deleted"
        cursor.execute(sql, self._blogs._user["id"])
        return cursor.fetchall()