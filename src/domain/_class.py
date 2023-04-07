from uuid import uuid4
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from settings import Base


class Class(Base):
    __tablename__ = "class"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    index = Column(Integer)
    name = Column(String(255))
    project_id = Column(UUID(as_uuid=True), ForeignKey("project.id", ondelete="CASCADE"))