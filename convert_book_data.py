import json
from get_summary import GetSummary

# 本の情報をjson形式に変換してフォルダーに格納するクラス
class ConvertBookData:

    def __init__(self, book_lists, folder_path):
        self.book_lists = book_lists
        self.folder_path = folder_path

    def convert(self):
        # 複数の本のデータが「タイトル、ISBNコード」の順で二次元配列で渡される
        for data in self.book_lists:
            dict_book = {}
            title = data[0]
            ISBN = data[1]

            # ISBNコードを使用してAPIを叩き本の要約を取得する
            summary = GetSummary(ISBN).get_suumary()

            # 空の辞書にデータをそれぞれ格納する
            dict_book["title"] = title
            dict_book["summary"] = summary

            # 指定されたフォルダーにISBNコードをファイル名としてデータを格納する
            # データは辞書型からjson形式に変換する
            with open(f"{self.folder_path}/{ISBN}.json", "w", encoding="utf-8") as f:
                json.dump(dict_book, f, indent=4, ensure_ascii=False)
