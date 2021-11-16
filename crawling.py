import feedparser
from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials
import datetime
from dotenv import load_dotenv
import os




# ニュース記事のデータを取得するためのクラス
class CrawlingNews:

    def __init__(self, rss_url):
        self.rss_url = rss_url

    def crawling(self):
        data = feedparser.parse(self.rss_url)
        news = [[entry.title, entry.summary] for entry in data.entries]

        return news



# Firebaseにデータを追加するためのクラス
class AddFirebase:

    def __init__(self, news_list, json_path):
        self.news_list = news_list
        self.json_path = json_path

    def add_database(self):
        cred = credentials.Certificate(self.json_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        datetime_now = datetime.datetime.now()
        formated_time = datetime_now.strftime("%Y年%m月%d日%H時%M分")
        collection_name = f"news_{formated_time}"

        for data in self.news_list:
            try:
                title = data[0]
                summary = data[1]

                doc_ref = db.collection(collection_name)

                doc_ref.add({
                    "title": title,
                    "summary": summary,
                })
            except:
                pass

        return collection_name




# ニュース記事のRSSのURL
URL = "https://www.news24.jp/rss/index.rdf"


# FirebaseのAPIキー
load_dotenv()
JSON_PATH = os.environ["FIREBASE_API_KEY"]

news_data = CrawlingNews(URL)
news_list = news_data.crawling()
add_firebase = AddFirebase(news_list, JSON_PATH)
add_firebase.add_database()
