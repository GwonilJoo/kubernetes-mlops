from uuid import UUID
from typing import List

from src.domain._class import BaseClass, Class
from src.requests._class import ClassRequest
from src.repository._class import IClassRepository

class ClassUseCase:
    def __init__(self, repo: IClassRepository):
        self.repo = repo

    def create(self, request: ClassRequest) -> List[Class]:
        for i, name in enumerate(request.names):
            req = BaseClass(
                index=i,
                name=name,
                project_id=request.project_id,
            )
            self.repo.create(req)
            
        class_list: List[Class] = self.read_by_project_id(request.project_id)
        return class_list
    
    def read_all(self) -> List[Class]:
        class_list: List[Class] = self.repo.read_all()
        return class_list
    
    def read(self, id: UUID) -> Class:
        filters = {"id": id}
        class_: Class = self.repo.read(filters)[0]
        return class_
    
    def read_by_project_id(self, project_id) -> List[Class]:
        filters = {"project_id": project_id}
        class_list: List[Class] = self.repo.read(filters)
        return class_list
    
    def delete(self, id: UUID) -> Class:
        class_: Class = self.repo.read(id)
        self.repo.delete(id)
        return class_