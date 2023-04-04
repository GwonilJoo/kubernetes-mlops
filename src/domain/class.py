from pydantic import Field
from uuid import uuid4, UUID

from src.utils import DTO


class Class(DTO):
    id: UUID = Field(default_factory=uuid4)
    index: int
    name: str
    project_id: UUID = Field(default_factory=uuid4)