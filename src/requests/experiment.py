from pydantic import Field
from uuid import uuid4, UUID
from enum import auto
from bson import ObjectId

from src.utils import DTO, StrEnum
from src.domain.experiment import Result


class ModelType(StrEnum):
    resnet18 = auto()


class ExperimentCreate(DTO):
    model: ModelType
    epochs: int
    learning_rate: float
    batch_size: int


class Experiment(DTO):
    _id: ObjectId
    model: ModelType
    epochs: int
    learning_rate: float
    batch_size: int
    result : Result
    project_id: UUID = Field(default_factory=uuid4)
