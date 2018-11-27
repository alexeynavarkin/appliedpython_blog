import pymysql


connection =\
    pymysql.connect(
        host='localhost',
        user="root",
        password="root",
        db="blog",
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)

def set_child_post(cursor: pymysql.cursors.DictCursor, comment_id, post_id):
    sql = "SELECT * FROM Comment WHERE Comment_id=%s"
    cursor.execute(sql, comment_id)
    comments = cursor.fetchall()
    for comment in comments:
        set_child_post(cursor, comment['id'], post_id)
        print(f"SETTING {post_id} FOR COMMENT {comment['id']}", flush=True)
        sql = "UPDATE Comment SET Post_id=%s WHERE id=%s"
        cursor.execute(sql,(post_id, comment['id']))

def fill_post(cursor: pymysql.cursors.DictCursor):
    sql = "SELECT * FROM Comment WHERE Post_id IS NOT NULL"
    cursor.execute(sql)
    comments = cursor.fetchall()
    for comment in comments:
        print("NEW TREE")
        set_child_post(cursor, comment['id'], comment['Post_id'])

fill_post(connection.cursor())
connection.commit()
