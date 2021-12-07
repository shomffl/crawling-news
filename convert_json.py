import json

class ConvertJson:

    def __init__(self, news_data, file_path):
        self.news_data = news_data
        self.file_path = file_path

    def convert(self):
        news_dict = {}
        for num, data in enumerate(self.news_data):
            filename = f"news{num}"
            news_dict[filename] = dict((["title", data[0]],["summary", data[1]],["link", data[2]]))

        with open(self.file_path , "w") as f:
            data = json.dumps(news_dict, sort_keys=True, indent=4)
            f.write(data)

        return news_dict
