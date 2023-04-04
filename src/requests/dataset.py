from pydantic import Field
from uuid import uuid4, UUID
from typing import List
from typing_extensions import Annotated
from fastapi import File, UploadFile

from src.utils import DTO

class UploadRequest(DTO):
    images: Annotated[List[UploadFile], File]
    class_id: UUID = Field(default_factory=uuid4)
    #class_id: str