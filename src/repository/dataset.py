from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List, Dict, Optional
from sqlalchemy.orm import Session

from src.domain.dataset import Dataset
from src.requests.dataset import CreateDataset


class IDatasetRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self, db: Session, req: CreateDataset) -> Dataset:
        pass

    @abstractmethod
    def read(self, db: Session, id: UUID) -> Optional[Dataset]:
        pass

    @abstractmethod
    def read_by_filters(self, db: Session, filters: Optional[Dict[str, any]]) -> List[Dataset]:
        pass

    @abstractmethod
    def delete(self, db: Session, id: UUID) -> Dataset:
        pass