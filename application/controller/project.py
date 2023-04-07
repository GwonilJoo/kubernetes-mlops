from fastapi import APIRouter, Depends
from uuid import UUID
from typing import List
from sqlalchemy.orm import Session

from src.domain import project as models
from src.use_cases.project import ProjectUseCase
from src.requests import project as schemas
from application.repository.project import ProjectMariadb
from src.utils import get_db
from settings import Base, engine

models.Base.metadata.create_all(bind=engine)

repo = ProjectMariadb()
project_router = APIRouter()
project_use_case = ProjectUseCase(repo)


@project_router.post("")
async def create(req: schemas.ProjectCreate, db: Session = Depends(get_db)) -> schemas.Project:
    project: models.Project = project_use_case.create(db, req)
    return project

@project_router.get("")
async def read_all(db: Session = Depends(get_db)) -> List[schemas.Project]:
    project_list: List[models.Project] = project_use_case.read_all(db)
    return project_list

@project_router.get("/{project_id}")
async def read(project_id: UUID, db: Session = Depends(get_db)) -> schemas.Project:
    project: models.Project = project_use_case.read(db, project_id)
    return project

@project_router.delete("/{project_id}")
async def delete(project_id: UUID, db: Session = Depends(get_db)) -> schemas.Project:
    project: models.Project = project_use_case.delete(db, project_id)
    return project