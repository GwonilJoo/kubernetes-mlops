from fastapi import APIRouter, File, UploadFile
from uuid import UUID, uuid4
from typing import List
from typing_extensions import Annotated

from src.domain._class import Class
from src.domain.dataset import Dataset, DatasetType
from src.use_cases.dataset import DatasetUseCase
from src.requests.dataset import UploadRequest
from application.repository.dataset import DatasetMemRepo
from application.controller._class import class_use_case

dataset_router = APIRouter()
repo = DatasetMemRepo()
dataset_use_case = DatasetUseCase(repo)


@dataset_router.post("/")
async def create(
    class_id: UUID, 
    type: DatasetType, 
    images: Annotated[List[UploadFile], File]) -> List[Dataset]:
    #class_: Class = class_use_case.read(class_id)

    req = UploadRequest(
        #project_id=class_.project_id,
        project_id=uuid4(),
        class_id=class_id,
        class_name="dog",
        #class_name=class_.name,
        type=type,
        images=images
    )
    dataset_list: List[Dataset] = dataset_use_case.upload(req)
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