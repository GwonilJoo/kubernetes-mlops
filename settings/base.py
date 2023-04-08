from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings
import os

# save dir
class Settings(BaseSettings):
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    RELOAD = True if os.getenv("RELOAD", "true") == "true" else False
    WORKERS = int(os.getenv("WORKERS", "1"))
    DATASET_DIR = os.getenv("DATASET_DIR", "./saved/dataset")
    MODEL_DIR = os.getenv("MODEL_DIR", "./saved/models")

    # MongoDB
    MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
    MONGO_PORT = int(os.getenv("MONGO_PORT", "31000"))
    MONGO_DB = os.getenv("MONGO_DB", "mlops")

    # MariaDB
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@0.0.0.0:3306/dev"


settings = Settings()

ENGINE = create_engine(
    settings.SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
BASE = declarative_base()