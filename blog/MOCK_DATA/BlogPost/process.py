import csv
import random

with open("BLOGPOST_MOCK_DATA.csv", "w") as write_file:
    writer = csv.writer(write_file)
    #write header
    writer.writerow(["id", "Blog_id", "Post_id"])
    #write data
    for idx in range(1,10001):
        writer.writerow([idx, random.randint(1,100), idx])