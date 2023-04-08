from settings import (
    SessionLocal, BASE, ENGINE
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def set_database():
    BASE.metadata.create_all(bind=ENGINE)
