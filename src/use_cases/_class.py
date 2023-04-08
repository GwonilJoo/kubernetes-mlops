from uuid import UUID
from typing import List
from sqlalchemy.orm import Session
import os
import shutil

from src.domain._class import Class
from src.requests._class import ClassCreate, ClassCreateMany
from src.requests.dataset import DatasetType
from src.repository._class import IClassRepository
from settings import Settings

class ClassUseCase:
    def __init__(self, repo: IClassRepository, settings: Settings):
        self.dataset_dir = settings.DATASET_DIR
        self.repo = repo

    def create(self, db: Session, request: ClassCreateMany) -> List[Class]:
        for i, name in enumerate(request.names):
            req = ClassCreate(
                index=i,
                name=name,
                project_id=request.project_id,
            )
            self.repo.create(db, req)
            
        class_list: List[Class] = self.read_by_project_id(db, request.project_id)
        return class_list
    
    def read_all(self, db: Session) -> List[Class]:
        class_list: List[Class] = self.repo.read_by_filters(db)
        return class_list
    
    def read(self, db: Session, id: UUID) -> Class:
        class_: Class = self.repo.read(db, id)
        return class_
    
    def read_by_project_id(self, db: Session, project_id) -> List[Class]:
        filters = {"project_id": project_id}
        class_list: List[Class] = self.repo.read_by_filters(db, filters)
        return class_list
    
    def delete(self, db: Session, id: UUID) -> Class:
        class_: Class = self.repo.read(db, id)
        self.repo.delete(db, id)

        train_dataset_dir = os.path.join(
            self.dataset_dir, 
            str(class_.project_id), 
            DatasetType.TRAIN,
            str(class_.name)
        )

        test_dataset_dir = os.path.join(
            self.dataset_dir, 
            str(class_.project_id), 
            DatasetType.TEST,
            str(class_.name)
        )

        shutil.rmtree(train_dataset_dir)
        shutil.rmtree(test_dataset_dir)
        return class_