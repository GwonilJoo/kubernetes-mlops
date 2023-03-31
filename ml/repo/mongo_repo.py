from pymongo import MongoClient
from datetime import datetime
from dataclasses import asdict

class MongoRepo:
    def __init__(self, config):
        self.client = MongoClient(
            host=config.mongo["HOST"],
            port=config.mongo["PORT"],
            # username=config.mongo["USERNAME"],
            # password=config.mongo["PASSWORD"],
        )
        self.db = self.client[config.mongo["DB_NAME"]]
        self.collection = self.db[config.mongo["COLLECTION"]]

    def create(self, data: dict):
        self.collection.insert_one(data)