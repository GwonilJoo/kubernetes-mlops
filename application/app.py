from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.utils import set_database

from application.controller import (
    project_router,
    class_router,
    dataset_router,
    experiment_router
)

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
app.include_router(experiment_router, prefix="/experiment")

set_database()

@app.get("/healthcheck")
async def healthcheck():
    return {"Hello": "World"}