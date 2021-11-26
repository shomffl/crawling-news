import json
import requests

class GetBookData:

    def __init__(self, ISBN):
        self.ISBN = ISBN

    def read(self):
        url = requests.get(f"https://api.openbd.jp/v1/get?isbn={self.ISBN}")
        text = url.text
        data = json.loads(text)[0]
        print(data)



# ISBNコードを引数として渡す
book = GetBookData("978-4101010137")
book.read()
