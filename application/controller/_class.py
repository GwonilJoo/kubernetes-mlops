from fastapi import APIRouter
from uuid import UUID
from typing import List

from src.domain._class import Class
from src.use_cases._class import ClassUseCase
from src.requests._class import ClassRequest
from application.repository._class import ClassMemRepo


repo = ClassMemRepo()
class_router = APIRouter()
class_use_case = ClassUseCase(repo)


@class_router.post("")
async def create(req: ClassRequest) -> List[Class]:
    class_: Class = class_use_case.create(req)
    return class_

@class_router.get("")
async def read_all() -> List[Class]:
    class_list: List[Class] = class_use_case.read_all()
    return class_list

@class_router.get("/")
async def read(project_id: UUID) -> List[Class]:
    class_list: List[Class] = class_use_case.read_by_project_id(project_id)
    return class_list

@class_router.get("/{id}")
async def read(id: UUID) -> Class:
    class_: Class = class_use_case.read(id)
    return class_

@class_router.delete("/{id}")
async def delete(id: UUID) -> Class:
    class_: Class = class_use_case.delete(id)
    return class_