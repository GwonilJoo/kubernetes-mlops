from fastapi import APIRouter, Depends
from uuid import UUID
from typing import List
from sqlalchemy.orm import Session

from src.domain import experiment as models
from src.use_cases.experiment import ExperimentUseCase
from src.requests import experiment as schemas
from application.repository.experiment import ExperimentMongoDB


repo = ExperimentMongoDB()
experiment_router = APIRouter()
experiment_use_case = ExperimentUseCase(repo)

@experiment_router.post("/{project_id}")
async def start_experiment(
    exp_list: List[schemas.ExperimentCreate], 
    project_id: UUID
) -> bool:
    res = experiment_use_case.start_experiment(exp_list, project_id)
    return res

@experiment_router.get("/{project_id}")
async def read_project_exp(project_id: UUID) -> List[schemas.Experiment]:
    exp_list: List[models.Experiment] = experiment_use_case.read_by_project_id(project_id)
    return exp_list