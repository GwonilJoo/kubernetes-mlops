from pydantic import Field
from uuid import uuid4, UUID
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from settings import BASE


class Project(BASE):
    __tablename__ = "project"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255))