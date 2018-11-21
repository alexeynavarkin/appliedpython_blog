from random import getrandbits
import csv

with open("COMMENT_MOCK_DATA", "r") as read_file,\
    open("COMMENT_MOCK_DATA.csv", "w") as write_file:
    data_read = csv.reader(read_file)
    data_write = csv.writer(write_file)
    data_write.writerow(["id", "data", "Post_id", "Comment_id", "User_id"])
    for idx, item in enumerate(data_read):
        item[0] = idx+1
        if getrandbits(1):
            item[2] = None
        else:
            item[3] = None
        data_write.writerow(item)
        print(f"\r{idx+1} values processed.", end="", flush=True)