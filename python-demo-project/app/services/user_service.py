from redis import Redis
from rq import Queue
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.models import User
from app.queue.tasks import send_welcome_email

redis_conn = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

queue = Queue(connection=redis_conn)


class UserService:

    @staticmethod
    def create_user(db: Session, name: str, email: str):
        user = User(name=name, email=email)

        db.add(user)
        db.commit()
        db.refresh(user)

        queue.enqueue(send_welcome_email, email)

        return user
