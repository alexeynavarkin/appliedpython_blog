from .blog_tools import SafeCursorMeta
from uuid import uuid4
#TODO: hash password check

class User(metaclass=SafeCursorMeta):
    def __init__(self, connection, blogs=None):
        self._connection = connection
        self._blogs = blogs

    def get(self, session_id, cursor=None):
        if session_id:
            sql = "SELECT u.* FROM Session s JOIN User u ON s.user_id = u.id WHERE s.id=%s"
            cursor.execute(sql, session_id)
            if cursor.rowcount:
                return cursor.fetchone()
            else:
                raise ValueError("Wrong username or password.")
        else:
            raise RuntimeError("Unauthorised.")

    def create(self, username, password, first_name, last_name, cursor=None):
        sql = "SELECT * FROM User WHERE username=%s"
        cursor.execute(sql, username)
        if cursor.rowcount:
            raise ValueError(f"User with username '{username}' already exists.")
        sql = "INSERT INTO User (username, password, first_name, last_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (username, password, first_name, last_name))

    def auth(self, username, password, cursor=None):
        sql = "SELECT * FROM User WHERE username=%s;"
        cursor.execute(sql, username)
        if not cursor.rowcount:
            raise ValueError(f"User with username '{username}' not exists.")
        user = cursor.fetchone()
        if user["password"] == password:
            session_id = str(uuid4())
            sql = "INSERT INTO Session (user_id, id) VALUES (%s, %s)"
            cursor.execute(sql, (user["id"], session_id))
            return session_id
        else:
            raise ValueError("User auth failed.")

    def list(self, cursor=None):
        sql = "SELECT * FROM User"
        cursor.execute(sql)
        return cursor.fetchall()