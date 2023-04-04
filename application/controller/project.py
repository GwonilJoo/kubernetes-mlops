from fastapi import APIRouter
from uuid import UUID
from typing import List

from src.domain.project import Project
from src.use_cases.project import ProjectUseCase
from src.requests.project import ProjectRequest
from application.repository.project import ProjectMemRepo


repo = ProjectMemRepo()
project_router = APIRouter()
project_use_case = ProjectUseCase(repo)


@project_router.post("")
async def create(req: ProjectRequest) -> Project:
    project: Project = project_use_case.create(req)
    return project

@project_router.get("")
async def read_all() -> List[Project]:
    project_list: List[Project] = project_use_case.read_all()
    return project_list

@project_router.get("/{project_id}")
async def read(project_id: UUID) -> Project:
    project: Project = project_use_case.read(project_id)
    return project

@project_router.delete("/{project_id}")
async def delete(project_id: UUID) -> Project:
    project: Project = project_use_case.delete(project_id)
    return project