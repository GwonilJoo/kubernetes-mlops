from typing import List
import shutil
import os
from sqlalchemy.orm import Session

from src.requests.dataset import CreateDatasetMany, CreateDataset
from src.domain.dataset import Dataset
from src.repository.dataset import IDatasetRepository

class DatasetUseCase:
    def __init__(self, repo: IDatasetRepository):
        self.repo = repo
        self.root = './saved'

    def upload(self, db: Session, req: CreateDatasetMany) -> List[Dataset]:
        dir = os.path.join(self.root, str(req.project_id), req.type, str(req.class_name))
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