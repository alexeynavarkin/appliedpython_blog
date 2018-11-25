from random import getrandbits, randint
from requests import get
from time import sleep
import csv

with open("COMMENT_MOCK_DATA", "w") as write_file:
    for idx in range(0, 100):
        response = get("https://api.mockaroo.com/api/ed04e710?count=1000&key=86b1af70")
        data = response.text
        write_file.write(data)
        print(f"\r{idx+1}/{100} blocks downloaded.", end="", flush=True)

with open("COMMENT_MOCK_DATA", "r") as read_file,\
    open("COMMENT_MOCK_DATA.csv", "w") as write_file:
    data_read = csv.reader(read_file)
    data_write = csv.writer(write_file)
    data_write.writerow(["id", "data", "Post_id", "Comment_id", "User_id"])
    for idx, item in enumerate(data_read):
        item[0] = idx+1
        item[3] = randint(0, idx)
        if getrandbits(1) and item[0] != item[3] and int(item[3]) != 0:
            item[2] = None
        else:
            item[3] = None
        data_write.writerow(item)
        print(f"\r{idx+1} values processed.", end="", flush=True)
