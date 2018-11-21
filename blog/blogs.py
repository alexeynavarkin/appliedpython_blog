from .user import User
import pymysql
#TODO: hash password check

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Blogs(metaclass=Singleton):
    def init(self):
        self._connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='root',
                                          db='blog',
                                          charset='utf8',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.user = User(self._connection)

    def comment_create(self):
        pass

    def comment_list(self):
        pass

    def comment_list_tree(self):
        #TODO: additionaly
        pass

    def comment_list_blog_user(self):
        # TODO: additionaly
        pass