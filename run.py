from dotenv import load_dotenv
import os
from crawling import CrawlingNews
from convert_json import ConvertJson
import datetime



# ニュース記事のRSSのURL
URL = "https://www.news24.jp/rss/index.rdf"

# FirebaseのAPIキー
load_dotenv()
JSON_PATH = os.environ["FIREBASE_API_KEY"]

news_data = CrawlingNews(URL)
news_list = news_data.crawling()

# 現在時刻の取得
datetime_now = datetime.datetime.now()

# 取得した現在時刻を任意のフォーマットに変更
formated_time = datetime_now.strftime("%Y年%m月%d日%H時%M分%S秒")

file_name= f"news_{formated_time}"

file_path = f"./news_files/{file_name}.json"

json_data = ConvertJson(news_list, file_path)
json_data.convert()
