from requests import get
from time import sleep


with open("COMMENT_MOCK_DATA", "w") as write_file:
    for idx in range(0, 100):
        response = get("https://api.mockaroo.com/api/ed04e710?count=1000&key=86b1af70")
        data = response.text
        write_file.write(data)
        print(f"\r{idx+1} blocks downloaded.", end="", flush=True)
        sleep(0.5)