from abc import ABCMeta, abstractmethod
from uuid import UUID
from typing import List
from sqlalchemy.orm import Session

from src.domain.project import Project
from src.requests.project import ProjectCreate


class IProjectRepository(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create(self, db: Session, project: ProjectCreate) -> Project:
        pass

    @abstractmethod
    def read_all(self, db: Session) -> List[Project]:
        pass

    @abstractmethod
    def read(self, db: Session, id: UUID) -> Project:
        pass

    @abstractmethod
    def delete(self, db: Session, id: UUID) -> None:
        pass
    