from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List, Dict, Optional
from sqlalchemy.orm import Session

from src.domain._class import Class
from src.requests._class import ClassCreate


class IClassRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self, db: Session, req: ClassCreate) -> Class:
        pass

    @abstractmethod
    def read(self, db: Session, id: UUID) -> Optional[Class]:
        pass

    @abstractmethod
    def read_by_filters(self, db: Session, filters: Dict[str, any] = {}) -> List[Class]:
        pass

    @abstractmethod
    def delete(self, db: Session, id: UUID) -> None:
        pass
    