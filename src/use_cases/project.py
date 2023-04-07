from uuid import UUID
from typing import List
from sqlalchemy.orm import Session

from src.domain.project import Project
from src.requests.project import ProjectCreate
from src.repository.project import IProjectRepository

class ProjectUseCase:
    def __init__(self, repo: IProjectRepository):
        self.repo = repo

    def create(self, db: Session, req: ProjectCreate) -> Project:
        project: Project = self.repo.create(db, req)
        return project
    
    def read_all(self, db: Session) -> List[Project]:
        project_list: List[Project] = self.repo.read_all(db)
        return project_list
    
    def read(self, db: Session, id: UUID) -> Project:
        project: Project = self.repo.read(db, id)
        return project
    
    def delete(self, db: Session, id: UUID) -> Project:
        project: Project = self.repo.read(db, id)
        self.repo.delete(db, id)
        return project