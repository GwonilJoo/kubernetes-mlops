from uuid import UUID

from src.utils import DTO

class ProjectCreate(DTO):
    name: str


class Project(ProjectCreate):
    id: UUID
    name: str

    class Config:
        orm_mode = True