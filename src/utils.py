from enum import Enum
from pydantic import BaseModel, BaseConfig
from settings import SessionLocal, Base, engine

class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.value
    

class DTO(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def set_database():
    Base.metadata.create_all(bind=engine)
