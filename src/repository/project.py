from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List

from src.domain.project import Project
from src.requests.project import ProjectRequest


class IProjectRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self, project: ProjectRequest) -> UUID:
        pass

    @abstractmethod
    def read_all(self) -> List[Project]:
        pass

    @abstractmethod
    def read(self, id: UUID) -> Project:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> Project:
        pass
    