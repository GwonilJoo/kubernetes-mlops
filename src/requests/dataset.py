from pydantic import Field
from uuid import uuid4, UUID
from typing import List
from typing_extensions import Annotated
from fastapi import File, UploadFile

from src.utils import DTO, StrEnum


class DatasetType(StrEnum):
    TRAIN = "train"
    TEST = "test"


class UploadDataset(DTO):
    class_id: UUID = Field(default_factory=uuid4)
    class_name: str
    type: DatasetType
    images: Annotated[List[UploadFile], File]


class CreateDatasetMany(DTO):
    project_id: UUID = Field(default_factory=uuid4)
    class_id: UUID = Field(default_factory=uuid4)
    class_name: str
    type: DatasetType
    images: Annotated[List[UploadFile], File]


class CreateDataset(DTO):
    type: DatasetType
    path: str
    class_id: UUID


class Dataset(DTO):
    id: UUID
    type: DatasetType
    path: str
    class_id: UUID

    class Config:
        orm_mode = True
