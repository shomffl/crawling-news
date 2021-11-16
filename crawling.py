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
        # ニュース記事のRSSからタイトルと要約を取得してリストに格納する。
        data = feedparser.parse(self.rss_url)
        news = [[entry.title, entry.summary] for entry in data.entries]

        return news



# Firebaseにデータを追加するためのクラス
class AddFirebase:

    def __init__(self, news_list, json_path):
        self.news_list = news_list
        self.json_path = json_path

    def add_database(self):

        # Firebaseの初期化
        cred = credentials.Certificate(self.json_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        # 現在時刻の取得
        datetime_now = datetime.datetime.now()

        # 取得した現在時刻を任意のフォーマットに変更
        formated_time = datetime_now.strftime("%Y年%m月%d日%H時%M分")

        # Firestoreのcollectionの名前を"news_{現在時刻}"という形式にする
        collection_name = f"news_{formated_time}"

        for data in self.news_list:
            try:
                title = data[0]
                summary = data[1]

                # Firestoreにアクセスして上記のcollection_name変数に格納した名前のcollectionを作成する。
                # Firestoreの場合、指定されたコレクションが存在しない場合は、自動的に生成される。
                doc_ref = db.collection(collection_name)

                # collectionにタイトルと要約を追加していく。
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
