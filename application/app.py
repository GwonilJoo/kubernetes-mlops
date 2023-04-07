from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from typing_extensions import Annotated
from uuid import uuid4, UUID

from src.use_cases import (
    ExperimentUseCase
)
from src.use_cases.experiment import ExperimentUseCase
from src.requests.experiment import ExperimentRequest, ExperimentListRequest
from src.utils import set_database

from application.controller.project import project_router
from application.controller._class import class_router
from application.controller.dataset import dataset_router


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
app.include_router(class_router, prefix="/class")
app.include_router(dataset_router, prefix="/dataset")

set_database()

experiment_use_case = ExperimentUseCase()



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


# @app.post("/dataset/{class_id}")
# async def upload_dataset(
#     images: Annotated[
#         List[UploadFile], File(description="Multiple files as UploadFile")
#     ],
#     class_id: UUID
# ) -> Dict[str, List[str]]:
#     req = UploadRequest(images=images, class_id=class_id)
#     filenames: List[str] = dataset_use_case.upload(req)
#     return {"filenames": filenames}