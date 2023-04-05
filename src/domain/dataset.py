from pydantic import Field
from uuid import uuid4, UUID
from enum import auto

from src.utils import DTO, StrEnum


class DatasetType(StrEnum):
    TRAIN = "train"
    TEST = "test"


class CreateDataset(DTO):
    path: str
    class_id: UUID = Field(default_factory=uuid4)
    type: DatasetType


class Dataset(CreateDataset):
    id: UUID = Field(default_factory=uuid4)