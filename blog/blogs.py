from .user import User
from .comment import Comment
from .post import Post
from .blog import Blog
import pymysql


class Blogs:
    def init(self):
        self._connection = pymysql.connect(host='localhost',
                                           user='root',
                                           password='root',
                                           db='blog',
                                           charset='utf8',
                                           cursorclass=pymysql.cursors.DictCursor)
        self.user = User(self._connection, self)
        self.blog = Blog(self._connection, self)
        self._session = None
        self._user = None

    def auth(self, username, password):
        self._session = self.user.auth(username, password)
        self._user = self.user.get(self._session)