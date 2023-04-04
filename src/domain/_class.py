from pydantic import Field
from uuid import uuid4, UUID

from src.utils import DTO


class BaseClass(DTO):
    index: int
    name: str
    project_id: UUID = Field(default_factory=uuid4)


class Class(BaseClass):
    id: UUID = Field(default_factory=uuid4)