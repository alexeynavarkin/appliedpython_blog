from time import sleep
from unittest import TestCase
import blog


class TestUser(TestCase):
    blog.truncate_table("User")
    blog.apply_csv("User", "blog/MOCK_DATA/User/USER_MOCK_DATA.csv")

    def test_user(self):
        b = blog.Blogs()
        b.init()
        b.user.create("test_user", "test_password", "Testname", "Testlname")
        with self.assertRaises(ValueError):
            b.user.create("test_user", "test_password", "Testname", "Testlname")

    def test_user_list(self):
        b = blog.Blogs()
        b.init()
        users = b.user.list()
        self.assertEqual(1001,len(users))
        self.assertTrue(any(user["username"]=="test_user" and \
                            user["password"] == "test_password" and \
                            user["last_name"] == "Testlname" and \
                            user["first_name"] == "Testname"\
                            for user in users))

    def test_user_auth(self):
        b = blog.Blogs()
        b.init()
        users = b.user.list()