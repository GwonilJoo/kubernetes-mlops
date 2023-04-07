from uuid import UUID, uuid4
from typing import List, Optional, Dict
from sqlalchemy.orm import Session

from src.domain import _class as models
from src.requests import _class as schemas
from src.repository._class import IClassRepository

class Mariadb(IClassRepository):
    def __init__(self):
        pass
    
    def create(self, db: Session, req: schemas.ClassCreate) -> models.Class:
        class_ = models.Class(
            id=uuid4(),
            index=req.index,
            name=req.name,
            project_id=req.project_id,
        )
        db.add(class_)
        db.commit()
        db.refresh(class_)
        return class_
    
    def read(self, db: Session, id: UUID) -> Optional[models.Class]:
        return db.query(models.Class).filter(models.Class.id == id).first()
    
    def read_by_filters(self, db: Session, filters: Dict[str, any] = {}) -> List[models.Class]:
        return db.query(models.Class).filter_by(**filters).all()
    
    def delete(self, db: Session, id: UUID) -> None:
        db.query(models.Class).filter(models.Class.id == id).delete()
        db.commit()
