from pydantic import Field, BaseModel
from enum import auto
from uuid import uuid4, UUID
from typing import Optional

from src.utils import (
    StrEnum, DTO
)


class ModelType(StrEnum):
    SimpleCNN = auto()


class Activaton(StrEnum):
    SOFTMAX = auto()
    RELU = auto()
    TANH = auto()
    SIGMOID = auto()
    LINEAR = auto()


class ValuePath(BaseModel):
    value: float
    test_acc: float
    path: str


class Result(DTO):
    last_loss = ValuePath
    last_acc = ValuePath
    best_loss = ValuePath
    best_acc = ValuePath


class Experiment(DTO):
    id: UUID = Field(default_factory=uuid4)
    model: ModelType
    epochs: int
    learngin_rate: float
    batch_size: int
    #activation: Activaton
    #dropout: float
    result: Result
    project_id: UUID = Field(default_factory=uuid4)