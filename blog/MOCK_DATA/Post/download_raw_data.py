from requests import get
from time import sleep


with open("POST_MOCK_DATA", "w") as write_file:
    for idx in range(0, 10):
        response = get("https://api.mockaroo.com/api/e9f24d30?count=1000&key=86b1af70")
        data = response.text
        write_file.write(data)
        print(f"\r{idx+1} blocks downloaded.", end="", flush=True)
        sleep(0.5)