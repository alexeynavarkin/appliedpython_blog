from unittest import TestCase
import blog

bm = blog.BlogManager()
bm.create_structure()

class TestUser(TestCase):
    bm.truncate_table("User")
    bm.apply_csv("User", "blog/MOCK_DATA/User/USER_MOCK_DATA.csv")

    def test_user_create(self):
        b = blog.Blogs()
        b.init()
        b.user.create("test_user1", "test_password1", "Testname1", "Testlname1")
        b.auth("test_user1", "test_password1")

    def test_user_create_same_uname(self):
        b = blog.Blogs()
        b.init()
        b.user.create("test_user", "test_password", "Testname", "Testlname")
        with self.assertRaises(ValueError):
            b.user.create("test_user", "test_password", "Testname", "Testlname")

    def test_user_list(self):
        b = blog.Blogs()
        b.init()
        users = b.user.list()
        self.assertEqual(1002,len(users))
        self.assertTrue(any(user["username"]=="test_user" and \
                            user["password"] == "test_password" and \
                            user["last_name"] == "Testlname" and \
                            user["first_name"] == "Testname"\
                            for user in users))


class TestBlog(TestCase):
    bm = blog.BlogManager()
    bm.truncate_table("Blog")
    bm.apply_csv("Blog", "blog/MOCK_DATA/Blog/BLOG_MOCK_DATA.csv")

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
        self.assertFalse(any(bl["id"] == 45 for bl in b.blog.list_user()))
        self.assertFalse(any(bl["id"] == 45 for bl in b.blog.list()))


class TestPost(TestCase):
    bm = blog.BlogManager()
    bm.truncate_table("BlogPost")
    bm.truncate_table("Post")
    bm.apply_csv("Post", "blog/MOCK_DATA/Post/POST_MOCK_DATA.csv")
    bm.apply_csv("BlogPost", "blog/MOCK_DATA/BlogPost/BLOGPOST_MOCK_DATA.csv")

    def test_create(self):
        b = blog.Blogs()
        b.init()
        b.auth("btaunton1u", "yudD6qmd5I")
        b.post.create("Test_post", (1, 2, 3), "TestDATA")

    def test_create_wrong(self):
        b = blog.Blogs()
        b.init()
        b.auth("btaunton1u", "yudD6qmd5I")
        with self.assertRaises(ValueError):
            b.post.create("Test_post", (1, 2, 10002), "TestDATA")


class TestComment(TestCase):
    bm = blog.BlogManager()
    bm.truncate_table("Comment")
    bm.apply_csv("Comment", "blog/MOCK_DATA/Comment/COMMENT_MOCK_DATA.csv")

    def test_create(self):
        b = blog.Blogs()
        b.init()
        b.auth("btaunton1u", "yudD6qmd5I")
        with self.assertRaises(ValueError):
            b.comment.post(10002, "Test wrong comment")

    def test_tree(self):
        b = blog.Blogs()
        b.init()
        print(b.comment.list_tree(3))

    def test_list_blog_user(self):
        b = blog.Blogs()
        b.init()
        print(b.comment.list_blog_user([1,2],2))