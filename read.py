from firebase_admin import firestore
import firebase_admin
from firebase_admin import credentials



class ReadCollection:

    def __init__(self, collection_name, json_path):
        self.collection_name = collection_name
        self.json_path = json_path


    def read(self):
        # cred = credentials.Certificate(self.json_path)
        # firebase_admin.initialize_app(cred)
        db = firestore.client()

        docs = db.collection(self.collection_name).get()

        for doc in docs:
            data = doc.to_dict()
            print(data)
