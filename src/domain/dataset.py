from uuid import uuid4, UUID
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from settings import Base


class Dataset(Base):
    __tablename__ = "dataset"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    type = Column(String(50))
    path = Column(String(255))
    class_id = Column(UUID(as_uuid=True), ForeignKey("class.id", ondelete="CASCADE"))