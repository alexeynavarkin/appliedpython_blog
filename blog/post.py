from datetime import datetime
from .blog_tools import SafeCursorMeta


class Post(metaclass=SafeCursorMeta):
    def __init__(self, connection, blogs=None):
        # TODO: maybe move to parent class
        self._connection = connection
        self._blogs = blogs

    def check_auth(self):
        # TODO: move to parent class
        if not self._blogs._user:
            raise RuntimeError("Unauthorised.")

    def check_auth_post(self, post_id, cursor=None):
        self.check_auth()
        sql = "SELECT User_id FROM Post WHERE id=%s"
        cursor.execute(sql, post_id)
        if cursor.rowcount:
            post_user = cursor.fetchone()
            if not post_user["User_id"] == self._blogs._user["id"]:
                raise ValueError("Only owner can modify blog.")
        else:
            raise ValueError("No Blog with such name.")

    def create(self, post_name, blogs_id, data,cursor):
        self.check_auth()
        for blog_id in blogs_id:
            if not self._blogs.blog.get(blog_id):
                raise ValueError("One of specified blogs not exists.")
        sql = "INSERT INTO Post (post_name, user_id, data, post_date) "\
              "VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (post_name, self._blogs._user["id"], data,
                             datetime.now().strftime("%Y-%m-%d %H-%M-%S")))
        # DAT LOOKS LIKE UNSAFE, maybe move to stored procedure
        sql = "SELECT LAST_INSERT_ID() as id"
        cursor.execute(sql)
        post_id = cursor.fetchone()["id"]
        sql = "INSERT INTO BlogPost (Blog_id, Post_id) VALUES (%s, %s)"
        for blog_id in blogs_id:
            cursor.execute(sql, (blog_id, post_id))

    def edit(self, post_id, new_name, new_data, cursor=None):
        self.check_auth_post(post_id)
        sql = "UPDATE Post SET post_name=%s, data=%s WHERE id=%s"
        cursor.execute(sql, (new_name, new_data, post_id))
        if not cursor.rowcount:
            raise ValueError("No blog with such id.")

    def delete(self, blog_id, cursor=None):
        self.check_auth_post(blog_id)
        sql = "UPDATE Post SET deleted=1 WHERE id=%s"
        cursor.execute(sql, blog_id)
        if cursor.rowcount:
            raise ValueError("No blog with such id.")

