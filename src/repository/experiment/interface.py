from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List, Dict, Optional
from bson import ObjectId

from src.domain.experiment import Experiment


class IExperimentRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def read(self, id: ObjectId) -> Optional[Experiment]:
        pass

    @abstractmethod
    def read_by_filters(self, filters: Optional[Dict[str, any]]) -> List[Experiment]:
        pass

    @abstractmethod
    def delete(self, id: ObjectId) -> None:
        pass

    @abstractmethod
    def delete_many(self, filters: Optional[Dict[str, any]]) -> None:
        pass