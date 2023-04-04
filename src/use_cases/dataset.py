from fastapi import File, UploadFile
from typing_extensions import Annotated
from typing import List
import shutil
import os

from src.requests.dataset import UploadRequest


class DatasetUseCase:
    def __init__(self):
        self.root = './saved'
        #self.repo = repo

    def upload(
            self,
            req: UploadRequest
        ) -> List[str]:
        path_list = []
        for image in req.images:
            dir = os.path.join(self.root, str(req.class_id))
            #dir = os.path.join(self.root)
            path = os.path.join(dir, image.filename)

            if not os.path.exists(dir):
                os.makedirs(dir)
                os.chmod(dir, 0o755)

            with open(path, "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)
            path_list.append(path)
        return path_list