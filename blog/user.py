from .safe_cursor import SafeCursorMeta
from uuid import uuid4


class User(metaclass=SafeCursorMeta):
    def __init__(self, connection):
        self._connection = connection

    def create(self, username, password, first_name, last_name, cursor):
        sql = "SELECT * FROM blog.User WHERE username=%s"
        cursor.execute(sql, username)
        if cursor.rowcount:
            raise ValueError(f"User with username '{username}' already exists.")

        sql = "INSERT INTO blog.User (username, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (username, password, first_name, last_name))

    def auth(self, username, password, cursor):
        sql = "SELECT * FROM blog.User WHERE username=%s;"
        cursor.execute(sql, username)
        if not cursor.rowcount:
            raise ValueError(f"User with username '{username}' not exists.")
        user = cursor.fetchone()
        if user["password"] == password:
            sql = "INSERT INTO Session (user_id, id) VALUES (%s, %s)"
            sess_id = uuid4().int
            cursor.execute(sql,(user, sess_id))
            return sess_id
        else:
            raise ValueError("User auth failed.")

    def list(self, cursor):
        sql = "SELECT * FROM blog.User"
        cursor.execute(sql)
        return cursor.fetchall()