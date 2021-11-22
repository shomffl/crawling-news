# CRAWLING_NEWS

# 環境構築

```bash

pip install feedparser
pip install -U firebase-admin
pip install google-cloud-firestore
pip install python-dotenv

```
- firebaseでプロジェクトを作成して、認証ファイルを生成
- 生成した認証ファイルをルートディレクトリに置く
- ルートディレクトリに.envファイルを作成
- .envファイルに「FIREBASE_API_KEY=ダウンロードした認証ファイル名」 を追加
