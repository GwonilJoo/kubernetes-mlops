from uuid import UUID
from typing import List

from src.domain.project import Project
from src.requests.project import ProjectRequest
from src.repository.project import IProjectRepository

class ProjectUseCase:
    def __init__(self, repo: IProjectRepository):
        self.repo = repo

    def create(self, req: ProjectRequest) -> Project:
        id: UUID = self.repo.create(req)
        project: Project = self.repo.read(id)
        return project
    
    def read_all(self) -> List[Project]:
        project_list: List[Project] = self.repo.read_all()
        return project_list
    
    def read(self, id: UUID) -> Project:
        project: Project = self.repo.read(id)
        return project
    
    def delete(self, id: UUID) -> Project:
        project: Project = self.repo.read(id)
        self.repo.delete(id)
        return project