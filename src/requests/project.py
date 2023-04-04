from pydantic import Field
from uuid import uuid4, UUID
from typing import Optional
from enum import auto

from src.utils import DTO, StrEnum
from src.domain.experiment import Activaton, ModelType


class ProjectRequest(DTO):
    name: str
    dataset: str
