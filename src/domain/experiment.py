from uuid import UUID
from bson import ObjectId

from src.utils import DTO


class ValuePath(DTO):
    value: float
    test_acc: float
    path: str


class Result(DTO):
    last_loss = ValuePath
    last_acc = ValuePath
    best_loss = ValuePath
    best_acc = ValuePath


class ValuePath(DTO):
    _id: ObjectId    
    value: float
    test_acc: float
    path: str


class Result(DTO):
    _id: ObjectId
    best_loss: ValuePath
    best_acc: ValuePath
    last_loss: ValuePath
    last_acc: ValuePath


class Experiment(DTO):
    _id: ObjectId
    model: str
    epochs: int
    learning_rate: float
    batch_size: int
    result: Result
    project_id: UUID