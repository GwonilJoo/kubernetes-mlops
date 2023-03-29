from pydantic import BaseModel, Field
from enum import auto
from uuid import uuid4, UUID

from src.utils import StrEnum



class ModelType(StrEnum):
    SimpleCNN = auto()


class Activaton(StrEnum):
    SOFTMAX = auto()
    RELU = auto()
    TANH = auto()
    SIGMOID = auto()
    LINEART = auto()


class Experiment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    model: ModelType
    epoch: int
    activation: Activaton
    dropout: float
    save_path: str
    project_id: UUID = Field(default_factory=uuid4)

    class Config:
        arbitrary_types_allowed = True