from pydantic import Field
from uuid import uuid4, UUID
from typing import Optional
from enum import auto

from src.utils import DTO, StrEnum
from src.domain.experiment import Activaton, ModelType


class ExperimentRequest(DTO):
    model: ModelType
    epochs: int
    learning_rate: float
    batch_size: int
    #activation: Activaton
    #dropout: float
    save_dir: str
    #project_id: UUID = Field(default_factory=uuid4)


class LastBestEnum(StrEnum):
    LAST: auto()
    BEST: auto()


class LossAccEnum(StrEnum):
    LOSS: auto()
    ACC: auto()


class TrainTestEnum(StrEnum):
    TRAIN: auto()
    TEST: auto()


class ExperimentListRequest(DTO):
    project_id: Optional[UUID]
    model: Optional[ModelType]
    epochs: Optional[int]
    learning_rate: Optional[float]
    batch_size: Optional[int]
    #activation: Optional[Activaton]
    #dropout: Optional[float]
    train_test: Optional[TrainTestEnum]
    loss_acc: Optional[LossAccEnum]
    last_best: Optional[LastBestEnum]
