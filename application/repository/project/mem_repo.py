from uuid import UUID, uuid4
from typing import List

from src.domain.project import Project
from src.requests.project import ProjectRequest
from src.repository.project import IProjectRepository

class MemRepo(IProjectRepository):
    def __init__(self):
        self.data: List[Project] = []
    
    def create(self, req: ProjectRequest) -> UUID:
        project = Project(
            id=uuid4(),
            name=req.name,
        )
        self.data.append(project)
        return project.id
    
    def read_all(self) -> List[Project]:
        return self.data
    
    def read(self, id: UUID) -> Project:
        for project in self.data:
            if project.id == id:
                return project
    
    def delete(self, id: UUID) -> Project:
        for i, project in enumerate(self.data):
            if project.id == id:
                break
        project = self.data[i]
        del self.data[i]
        return project
