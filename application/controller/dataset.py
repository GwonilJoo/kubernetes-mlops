from fastapi import APIRouter, File, UploadFile, Depends
from uuid import UUID
from typing import List
from typing_extensions import Annotated
from sqlalchemy.orm import Session

from src.domain._class import Class
from src.domain import dataset as models
from src.use_cases.dataset import DatasetUseCase
from src.requests import dataset as schemas
from application.repository.dataset import DatasetMariadb
from application.controller._class import class_use_case
from src.utils import get_db
from settings import Base, engine


models.Base.metadata.create_all(bind=engine)

dataset_router = APIRouter()
repo = DatasetMariadb()
dataset_use_case = DatasetUseCase(repo)


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


# @dataset_router.delete("/{class_id}")
# async def delete(project_id: UUID) -> Project:
#     project: Project = project_use_case.delete(project_id)
#     return project