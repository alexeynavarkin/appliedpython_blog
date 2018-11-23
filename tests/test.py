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
        # TODO: check with patch
        b = blog.Blogs()
        b.init()
        b.auth("test_user", "test_password")
        self.assertTrue(b._session)
        self.assertTrue(b._user)


class TestBlog(TestCase):
    blog.truncate_table("Blog")
    blog.apply_csv("Blog", "blog/MOCK_DATA/Blog/BLOG_MOCK_DATA.csv")

    def test_blog(self):
        b = blog.Blogs()
        b.init()
        with self.assertRaises(RuntimeError):
            b.blog.edit(2, "Hmmm")
        b.auth("btaunton1u", "yudD6qmd5I")
        b.blog.edit(5, "Hmmm")

    def test_delete_unauth(self):
        b = blog.Blogs()
        b.init()
        with self.assertRaises(RuntimeError):
            b.blog.delete(45)

    def test_delete(self):
        b = blog.Blogs()
        b.init()
        b.auth("etillshi", "ko28nA0GsRH2")
        b.blog.delete(45)
        self.assertFalse(any(bl["id"]==45 for bl in b.blog.list_user()))
        self.assertFalse(any(bl["id"] == 45 for bl in b.blog.list()))