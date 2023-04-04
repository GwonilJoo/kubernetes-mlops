from pydantic import Field
from uuid import uuid4, UUID
from typing import List

from src.utils import DTO

class ClassRequest(DTO):
    names: List[str]
    project_id: UUID = Field(default_factory=uuid4)