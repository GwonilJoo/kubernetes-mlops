from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List, Dict

from src.domain._class import Class
from src.requests._class import ClassRequest


class IClassRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self, req: ClassRequest) -> UUID:
        pass

    @abstractmethod
    def read_all(self) -> List[Class]:
        pass

    @abstractmethod
    def read(self, filters: Dict[str, any]) -> Class:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> Class:
        pass
    