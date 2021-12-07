import json


# クローリングしたニュースのデータをjson形式にしてフォルダーに格納するクラス
class ConvertNewsData:

    def __init__(self, news_data, file_path):
        self.news_data = news_data
        self.file_path = file_path

    def convert(self):
        news_dict = {}

        # 引数とした渡されたニュースデータの二次元配列の順番とデータを取得
        for num, data in enumerate(self.news_data):

            # 対象のニュースが何番目かという情報を辞書のキーとして利用
            filename = f"news{num}"

            # 空の辞書にニュースのタイトル、要約、リンクを追加していく
            news_dict[filename] = dict((["title", data[0]],["summary", data[1]],["link", data[2]]))

        # 辞書型のデータをjson形式に変換して、指定されたパスに格納する
        with open(self.file_path , "w") as f:
            data = json.dumps(news_dict, sort_keys=True, indent=4)
            f.write(data)

        return news_dict
