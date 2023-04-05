from uuid import UUID, uuid4
from typing import List, Dict, Optional

from src.domain.dataset import CreateDataset, Dataset
from src.repository.dataset import IDatasetRepository

class MemRepo(IDatasetRepository):
    def __init__(self):
        self.data: List[Dataset] = []
    
    def create(self, req: CreateDataset) -> UUID:
        class_ = Dataset(
            id=uuid4(),
            **req.dict()
        )
        self.data.append(class_)
        return class_.id
    
    def read(self, id: UUID) -> Optional[Dataset]:
        for dataset in self.data:
            if dataset.id == id:
                return dataset
        return None
    
    def read_by_filters(self, filters: Optional[Dict[str, any]]=None) -> List[Dataset]:
        if not filters:
            return self.data
        
        result = self.data
        for key, value in filters.items():
            result = [x for x in result if x.dict()[key] == value]
        return result
    
    def delete(self, id: UUID) -> Dataset:
        for i, class_ in enumerate(self.data):
            if class_.id == id:
                break
        class_ = self.data[i]
        del self.data[i]
        return class_
