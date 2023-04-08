from typing import List
import shutil
import os
from sqlalchemy.orm import Session
from uuid import UUID

from src.requests.dataset import CreateDatasetMany, CreateDataset
from src.domain.dataset import Dataset
from src.repository.dataset import IDatasetRepository
from settings import Settings

class DatasetUseCase:
    def __init__(self, repo: IDatasetRepository, settings: Settings):
        self.repo = repo
        self.dataset_dir = settings.DATASET_DIR

    def upload(self, db: Session, req: CreateDatasetMany) -> List[Dataset]:
        dir = os.path.join(self.dataset_dir, str(req.project_id), req.type, str(req.class_name))
        if not os.path.exists(dir):
            os.makedirs(dir)
            os.chmod(dir, 0o755)
        
        res: List[Dataset] = []
        for image in req.images:
            path = os.path.join(dir, image.filename)
            with open(path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            
            data = CreateDataset(
                path=path,
                class_id=req.class_id,
                type=req.type
            )
            dataset = self.repo.create(db, data)
            res.append(self.repo.read(db, dataset.id))
        
        return res
    
    def delete(self, db: Session, id: UUID) -> Dataset:
        dataset: Dataset = self.repo.read(db, id)
        self.repo.delete(db, id)

        os.remove(dataset.path)
        return dataset