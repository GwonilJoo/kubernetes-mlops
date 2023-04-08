from uuid import UUID, uuid4
from typing import List, Optional
from sqlalchemy.orm import Session

from src.domain import project as models
from src.requests import project as schemas
from src.repository.project.interface import IProjectRepository

class MariaDB(IProjectRepository):
    def __init__(self):
        self.data: List[models.Project] = []
    
    def create(self, db: Session, req: schemas.ProjectCreate) -> models.Project:
        project = models.Project(
            id=uuid4(),
            name=req.name,
        )
        db.add(project)
        db.commit()
        db.refresh(project)
        return project
    
    def read_all(self, db: Session) -> List[models.Project]:
        return db.query(models.Project).all()
    
    def read(self, db: Session, id: UUID) -> Optional[models.Project]:
        return db.query(models.Project).filter(models.Project.id == id).first()
    
    def delete(self, db: Session, id: UUID) -> None:
        db.query(models.Project).filter(models.Project.id == id).delete()
        db.commit()
