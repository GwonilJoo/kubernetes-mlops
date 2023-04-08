from fastapi import APIRouter, File, UploadFile, Depends
from uuid import UUID
from typing import List
from typing_extensions import Annotated
from sqlalchemy.orm import Session

from src.domain._class import Class
from src.domain import dataset as models
from src.use_cases.dataset import DatasetUseCase
from src.requests import dataset as schemas
from src.repository.dataset import DatasetMariaDB
from application.controller._class import class_use_case
from application.utils import get_db 
from settings import settings


dataset_router = APIRouter()
repo = DatasetMariaDB()
dataset_use_case = DatasetUseCase(repo, settings)


@dataset_router.post("/")
async def create(
        class_id: UUID, 
        type: schemas.DatasetType, 
        images: Annotated[List[UploadFile], File],
        db: Session = Depends(get_db)
    ) -> List[schemas.Dataset]:
    class_: Class = class_use_case.read(db, class_id)

    req = schemas.CreateDatasetMany(
        project_id=class_.project_id,
        class_id=class_id,
        class_name=class_.name,
        type=type,
        images=images
    )
    dataset_list: List[models.Dataset] = dataset_use_case.upload(db, req)
    return dataset_list
1
# @dataset_router.get("/")
# async def read(project_id: UUID) -> List[Dataset]:
#     class_list: List[Class] = class_use_case.read_by_project_id(project_id)
#     dataset_list: List[Dataset] = dataset_use_case.get_project_dataset(class_list)
#     return dataset_list


# @dataset_router.get("/")
# async def read(class_id: UUID) -> List[Dataset]:
#     class_list: List[Class] = class_use_case.read_by_project_id(project_id)
#     dataset_list: List[Dataset] = dataset_use_case.read(project_id)
#     return project


@dataset_router.delete("/{id}")
async def delete(id: UUID, db: Session = Depends(get_db)) -> schemas.Dataset:
    dataset: models.Dataset = dataset_use_case.delete(db, id)
    return dataset