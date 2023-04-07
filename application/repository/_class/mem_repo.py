from uuid import UUID, uuid4
from typing import List, Dict, Optional

from src.domain._class import Class
from src.repository._class import IClassRepository

class MemRepo(IClassRepository):
    def __init__(self):
        self.data: List[Class] = []
    
    def create(self, req: Class) -> UUID:
        class_ = Class(
            id=uuid4(),
            **req.dict()
        )
        self.data.append(class_)
        return class_.id
    
    def read_all(self) -> List[Class]:
        return self.data
    
    def read(self, filters: Optional[Dict[str, any]]=None) -> List[Class]:
        if not filters:
            return self.data
        
        result = self.data
        for key, value in filters.items():
            result = [x for x in result if x.dict()[key] == value]
        return result
    
    def delete(self, id: UUID) -> Class:
        for i, class_ in enumerate(self.data):
            if class_.id == id:
                break
        class_ = self.data[i]
        del self.data[i]
        return class_
