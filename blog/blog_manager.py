from .blog_tools import SafeCursorMeta
from .settings import *
import pymysql
import csv


class BlogManager(metaclass=SafeCursorMeta):
    def __init__(self):
        self._connection =\
            pymysql.connect(host=host,
                            user=user,
                            password=password,
                            db=db,
                            charset='utf8',
                            cursorclass=pymysql.cursors.DictCursor)
        self.tables =\
         ({"table_name": "User", "file_name": "blog/MOCK_DATA/User/USER_MOCK_DATA.csv"},
          {"table_name": "Blog", "file_name": "blog/MOCK_DATA/Blog/BLOG_MOCK_DATA.csv"},
          {"table_name": "Post", "file_name": "blog/MOCK_DATA/Post/POST_MOCK_DATA.csv"},
          {"table_name": "BlogPost", "file_name": "blog/MOCK_DATA/BlogPost/BLOGPOST_MOCK_DATA.csv"},
          {"table_name": "Comment", "file_name": "blog/MOCK_DATA/Comment/COMMENT_MOCK_DATA.csv"},)


    def parse_sql(self, sql):
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
                # print(f"Parsed SQL: '{line.strip()}'.")

        return queries


    def create_structure(self, cursor=None):
        with open("blog/MOCK_DATA/structure/structure.sql") as sql:
            for query in self.parse_sql(sql.readlines()):
                cursor.execute(query)


    def truncate_table(self, table_name, cursor=None):
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
        for query in self.parse_sql(sql):
            cursor.execute(query)


    def replace_empty(self, table):
        for line in table:
            for idx in range(len(line)):
                if not line[idx]:
                    line[idx] = None
            yield line


    def apply_csv(self, table_name, file_name, cursor=None):
        with open(file_name, "r") as csv_data:
            print(f"Restoring table '{table_name}' from file '{file_name}'")
            reader = csv.reader(csv_data)
            header = reader.__next__()
            values = ",".join(header)
            sql = f"INSERT INTO {table_name}({values}) VALUES ({'%s'+',%s'*(len(header)-1)})"
            n_lines = cursor.executemany(sql, self.replace_empty(reader))
            print(f"Restored {n_lines} values.")

    def fill_data(self):
        for table in self.tables:
            self.apply_csv(**table)