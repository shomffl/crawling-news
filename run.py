from dotenv import load_dotenv
import os
from crawling import CrawlingNews
from add_news_data import AddNewsData
from read import ReadCollection
from get_collection_name import GetCollenctionName


# ニュース記事のRSSのURL
URL = "https://www.news24.jp/rss/index.rdf"

# FirebaseのAPIキー
load_dotenv()
JSON_PATH = os.environ["FIREBASE_API_KEY"]

news_data = CrawlingNews(URL)
news_list = news_data.crawling()
add_firebase = AddNewsData(news_list, JSON_PATH)
collection_name = add_firebase.add_database()
read_collection = ReadCollection(collection_name, JSON_PATH)
read_collection.read()
