from pydantic import Field
from uuid import uuid4, UUID

from src.utils import DTO


class Project(DTO):
    id: UUID = Field(default_factory=uuid4)
    name: str