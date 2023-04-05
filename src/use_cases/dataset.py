from fastapi import File, UploadFile
from typing_extensions import Annotated
from typing import List
import shutil
import os
from uuid import uuid4, UUID

from src.domain._class import Class
from src.requests.dataset import UploadRequest
from src.domain.dataset import CreateDataset, Dataset
from src.repository.dataset import IDatasetRepository

class DatasetUseCase:
    def __init__(self, repo: IDatasetRepository):
        self.repo = repo
        self.root = './saved'

    def upload(self, req: UploadRequest) -> List[Dataset]:
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
            id = self.repo.create(data)
            res.append(self.repo.read(id))
        
        return res