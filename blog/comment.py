from pymysql.err import IntegrityError
from .blog_tools import SafeCursorMeta


class Comment(metaclass=SafeCursorMeta):
    def __init__(self, connection, blogs=None):
        # TODO: maybe move to parent class
        self._connection = connection
        self._blogs = blogs
        self.depth = 0

    def check_auth(self):
        # TODO: move to parent class
        if not self._blogs._user:
            raise RuntimeError("Unauthorised.")

    def post(self, post_id, data, cursor=None):
        self.check_auth()
        sql = "INSERT INTO Comment (Post_id, User_id, data) " \
              "VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (post_id, self._blogs._user["id"], data))
        except IntegrityError:
            raise ValueError("No post with such id.")

    def comment(self, data, comment_id, cursor=None):
        self.check_auth()
        sql = "INSERT INTO Comment (Comment_id, User_id, data) " \
              "VALUES (%s, %s, %s)"
        try:
            cursor.execute(sql, (comment_id, self._blogs._user["id"], data))
        except IntegrityError:
            raise ValueError("No comment with such id.")

    def list_post(self, post_id, cursor=None):
        sql = "SELECT * FROM Comment WHERE Post_id=%s"
        cursor.execute(sql, post_id)
        return cursor.fetchall()

    def list_tree(self, comment_id, cursor=None):
        sql = "SELECT * FROM Comment WHERE id=%s"
        cursor.execute(sql, comment_id)
        if cursor.rowcount:
            tree = cursor.fetchone()
            tree["child"] = self.get_child(comment_id)
            return tree

    def get_child(self, comment_id, cursor=None):
        sql = "SELECT id, data FROM Comment WHERE Comment_id=%s"
        cursor.execute(sql, comment_id)
        if cursor.rowcount:
            comments = cursor.fetchall()
            for idx in range(len(comments)):
                comments[idx]["child"] = self.get_child(comments[idx]["id"])
            return comments

    def list_blog_user(self, users_ids, blog_id, cursor=None):
        if not users_ids:
            raise ValueError("Empty users field")
        sql = "SELECT c.* FROM Blog b " \
              "JOIN BlogPost bp ON b.id=bp.Blog_id " \
              "JOIN Post p ON p.id=bp.Post_id " \
              "JOIN Comment c ON c.Post_id=p.id " \
              f"WHERE c.User_id in ({'%s'+ ',%s'*(len(users_ids)-1)}) AND b.id=%s"
        cursor.execute(sql, tuple(users_ids) + (blog_id,))
        return cursor.fetchall()

