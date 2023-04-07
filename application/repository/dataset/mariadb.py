from uuid import UUID, uuid4
from typing import List, Optional, Dict
from sqlalchemy.orm import Session

from src.domain import dataset as models
from src.requests import dataset as schemas
from src.repository.dataset import IDatasetRepository

class Mariadb(IDatasetRepository):
    def __init__(self):
        pass
    
    def create(self, db: Session, req: schemas.CreateDataset) -> models.Dataset:
        dataset = models.Dataset(
            id=uuid4(),
            type=req.type,
            path=req.path,
            class_id=req.class_id
        )
        db.add(dataset)
        db.commit()
        db.refresh(dataset)
        return dataset
    
    def read(self, db: Session, id: UUID) -> Optional[models.Dataset]:
        return db.query(models.Dataset).filter(models.Dataset.id == id).first()
    
    def read_by_filters(self, db: Session, filters: Dict[str, any] = {}) -> List[models.Dataset]:
        return db.query(models.Dataset).filter_by(**filters).all()
    
    def delete(self, db: Session, id: UUID) -> None:
        db.query(models.Dataset).filter(models.Dataset.id == id).delete()
        db.commit()
