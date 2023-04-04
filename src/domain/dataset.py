from pydantic import Field
from uuid import uuid4, UUID
from enum import auto

from src.utils import DTO


class Dataset(DTO):
    id: UUID = Field(default_factory=uuid4)
    path: str
    class_id: UUID = Field(default_factory=uuid4)