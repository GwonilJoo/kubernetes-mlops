from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from typing_extensions import Annotated
from uuid import uuid4, UUID

from src.use_cases import (
    ProjectUseCase,
    DatasetUseCase,
    ExperimentUseCase
)
from src.use_cases.experiment import ExperimentUseCase
from src.use_cases.dataset import DatasetUseCase
from src.requests.experiment import ExperimentRequest, ExperimentListRequest
from src.requests.project import ProjectRequest
from src.requests.dataset import UploadRequest

from application.controller.project import project_router


app = FastAPI(
          title="Hubble AI API Scheduling Server",
          description="Hubble AI Scheduling Server",
          version="0.2.0",
      )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(project_router, prefix="/project")


experiment_use_case = ExperimentUseCase()
dataset_use_case = DatasetUseCase()



@app.get("/healthcheck")
async def healthcheck():
    return {"Hello": "World"}


@app.post("/experiment")
async def experiment(req: List[ExperimentRequest]) -> bool:
    res = experiment_use_case.start_experiment(req)
    return res


@app.get("/experiment/list")
async def experiment_list(req: ExperimentListRequest):
    pass


@app.post("/dataset/{class_id}")
async def upload_dataset(
    images: Annotated[
        List[UploadFile], File(description="Multiple files as UploadFile")
    ],
    class_id: UUID
) -> Dict[str, List[str]]:
    req = UploadRequest(images=images, class_id=class_id)
    filenames: List[str] = dataset_use_case.upload(req)
    return {"filenames": filenames}


@app.post("/project")
async def project(req: ProjectRequest):
    res = ProjectUseCase