from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List, Dict, Optional

from src.domain.dataset import Dataset, CreateDataset
from src.requests.dataset import UploadRequest


class IDatasetRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self, req: CreateDataset) -> UUID:
        pass

    @abstractmethod
    def read(self, id: UUID) -> Optional[Dataset]:
        pass

    @abstractmethod
    def read_by_filters(self, filters: Optional[Dict[str, any]]) -> List[Dataset]:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> Dataset:
        pass