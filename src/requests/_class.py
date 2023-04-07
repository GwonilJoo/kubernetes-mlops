from pydantic import Field
from uuid import uuid4, UUID
from typing import List

from src.utils import DTO


class ClassCreateMany(DTO):
    names: List[str]
    project_id: UUID = Field(default_factory=uuid4)


class ClassCreate(DTO):
    index: int
    name: str
    project_id: UUID


class Class(DTO):
    id: UUID
    index: int
    name: str
    project_id: UUID

    class Config:
        orm_mode = True