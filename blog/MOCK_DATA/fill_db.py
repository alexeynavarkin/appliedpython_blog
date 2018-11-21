import pymysql
import csv

def parse_sql(sql):
    queries = []
    DELIMITER = ';'
    query = ''

    for line in sql:
        if not line.strip():
            continue

        if line.startswith('--'):
            continue

        if 'DELIMITER' in line:
            DELIMITER = line.split()[1]
            continue

        if (DELIMITER not in line):
            query += line.replace(DELIMITER, ';')
            continue

        if query:
            query += line
            queries.append(query.strip())
            query = ''
        else:
            queries.append(line.strip())
    return queries


def create_structure():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='blog',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor,\
            open("structure/structure.sql") as sql:
        for query in parse_sql(sql.readlines()):
            cursor.execute(query)
    connection.commit()
    connection.close()


def truncate_table(table_name):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='blog',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        sql = ["SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;",
               "SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;",
               "SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';"]
        for query in sql:
            cursor.execute(query)
        sql = f"TRUNCATE blog.{table_name}"
        cursor.execute(sql)
        sql = ["SET SQL_MODE=@OLD_SQL_MODE;",
               "SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;",
               "SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;"]
        for query in parse_sql(sql):
            cursor.execute(query)
    connection.close()


def apply_csv(table_name, file_name):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='blog',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor,\
        open(file_name, "r") as csv_data:
        reader = csv.reader(csv_data)
        header = reader.__next__()
        values = ",".join(header)
        sql = f"INSERT INTO {table_name}({values}) VALUES ({'%s'+',%s'*(len(header)-1)})"
        for idx, query in enumerate(reader):
            for i in range(len(query)):
                if not query[i]:
                    query[i] = None
            cursor.execute(sql, query)
            print(f"\rExecuted {idx+1} queries.", end="", flush=True)
    print("")
    connection.commit()
    connection.close()


if __name__ == "__main__":
    tables = ({"table_name": "User", "file_name": "User/USER_MOCK_DATA.csv"},
              {"table_name": "Blog", "file_name": "Blog/BLOG_MOCK_DATA.csv"},
              {"table_name": "Post", "file_name": "Post/POST_MOCK_DATA.csv"},
              {"table_name": "BlogPost", "file_name": "BlogPost/BLOGPOST_MOCK_DATA.csv"},
              {"table_name": "Comment", "file_name": "Comment/COMMENT_MOCK_DATA.csv"},)
    try:
        create_structure()
        for table in tables:
            print(f"Filling {table['table_name']}.")
            apply_csv(**table)
    finally:
        connection.close()