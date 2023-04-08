import uvicorn
from application.app import app
from settings import settings

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        workers=settings.WORKERS,
    )