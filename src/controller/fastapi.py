from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import BackgroundTasks
from typing import Dict, List
import traceback

from src.use_cases.experiment import ExperimentUseCase
from src.requests.experiment import ExperimentRequest, ExperimentListRequest


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