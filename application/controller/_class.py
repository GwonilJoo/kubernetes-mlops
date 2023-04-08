from fastapi import APIRouter, Depends
from uuid import UUID
from typing import List
from sqlalchemy.orm import Session

from src.domain import _class as models
from src.use_cases._class import ClassUseCase
from src.requests import _class as schemas
from src.repository._class import ClassMariaDB
from application.utils import get_db
from settings import settings


repo = ClassMariaDB()
class_router = APIRouter()
class_use_case = ClassUseCase(repo, settings)


@class_router.post("")
async def create(req: schemas.ClassCreateMany, db: Session = Depends(get_db)) -> List[schemas.Class]:
    class_list: List[models.Class] = class_use_case.create(db, req)
    return class_list

@class_router.get("")
async def read_all(db: Session = Depends(get_db)) -> List[schemas.Class]:
    class_list: List[models.Class] = class_use_case.read_all(db)
    return class_list

@class_router.get("/")
async def read(project_id: UUID, db: Session = Depends(get_db)) -> List[schemas.Class]:
    class_list: List[models.Class] = class_use_case.read_by_project_id(db, project_id)
    return class_list

@class_router.get("/{id}")
async def read(id: UUID, db: Session = Depends(get_db)) -> schemas.Class:
    class_: models.Class = class_use_case.read(db, id)
    return class_

@class_router.delete("/{id}")
async def delete(id: UUID, db: Session = Depends(get_db)) -> schemas.Class:
    class_: models.Class = class_use_case.delete(db, id)
    return class_