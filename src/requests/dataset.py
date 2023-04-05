from pydantic import Field
from uuid import uuid4, UUID
from typing import List
from typing_extensions import Annotated
from fastapi import File, UploadFile

from src.utils import DTO
from src.domain.dataset import DatasetType


class UploadRequest(DTO):
    project_id: UUID = Field(default_factory=uuid4)
    class_id: UUID = Field(default_factory=uuid4)
    class_name: str
    type: DatasetType
    images: Annotated[List[UploadFile], File]