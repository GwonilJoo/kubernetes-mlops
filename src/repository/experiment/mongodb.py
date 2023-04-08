from uuid import UUID, uuid4
from typing import List, Optional, Dict
from pymongo import MongoClient
from bson import ObjectId

from src.domain import experiment as models
from src.repository.experiment.interface import IExperimentRepository


class MongoDB(IExperimentRepository):
    def __init__(self):
        host = "localhost"
        port = 31000
        db_name = "mlops"
        collection = "experiment"

        self.client = MongoClient(
            host=host,
            port=port,
            # username=config.mongo["USERNAME"],
            # password=config.mongo["PASSWORD"],
            uuidRepresentation='standard'
        )
        self.db = self.client[db_name]
        self.collection = self.db[collection]
    
    def read(self, id: ObjectId) -> Optional[models.Experiment]:
        return self.collection.find_one({"_id": id})
    
    def read_by_filters(self, filters: Dict[str, any] = {}) -> List[models.Experiment]:
        print(list(self.collection.find(filters)))
        return list(self.collection.find(filters))
    
    def delete(self, id: ObjectId) -> None:
        self.collection.delete_one({"_id": id})

    def delete_many(self, filters: Dict[str, any] = {}) -> None:
        self.collection.delete_many(filters)