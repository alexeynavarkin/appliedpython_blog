from random import getrandbits
import csv

with open("POST_MOCK_DATA", "r") as read_file,\
    open("POST_MOCK_DATA.csv", "w") as write_file:
    data_read = csv.reader(read_file)
    data_write = csv.writer(write_file)
    data_write.writerow(["id", "post_name", "post_date", "User_id", "data"])
    for idx, item in enumerate(data_read):
        item[0] = idx+1
        data_write.writerow(item)
        print(f"\r{idx+1} values processed.", end="", flush=True)