from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings
from app.db.database import Base
from app.db.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(router)
