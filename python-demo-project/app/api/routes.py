from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.clients.external_client import external_client
from app.db.database import get_db
from app.schemas.user_schema import UserCreate
from app.services.user_service import UserService

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/users")
def create_user(
    payload: UserCreate,
    db: Session = Depends(get_db)
):
    user = UserService.create_user(
        db,
        payload.name,
        payload.email
    )

    return user


@router.get("/external-posts")
async def external_posts():
    data = await external_client.get_posts()
    return data
