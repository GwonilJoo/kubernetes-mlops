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
    MARIA_HOST = os.getenv("MARIADB", "localhost")
    MARIA_PORT = os.getenv("MARIA_PORT", "3306")
    MARIA_USER = os.getenv("MARIA_USER", "root")
    MARIA_PWD = os.getenv("MARIA_PWD", "1234")
    MARIA_DB = os.getenv("MARIA_DB", "dev")
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@0.0.0.0:31001/dev"


settings = Settings()

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{settings.MARIA_USER}:{settings.MARIA_PWD}@{settings.MARIA_HOST}:{settings.MARIA_PORT}/{settings.MARIA_DB}"
ENGINE = create_engine(
    settings.SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
BASE = declarative_base()