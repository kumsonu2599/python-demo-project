from app.db.repositories.user_repository import UserRepository
from app.queue.queue_service import QueueService


class UserService:

    @staticmethod
    def create_user(name: str, email: str):

        user = UserRepository.create_user(
            name=name,
            email=email
        )

        QueueService.send_welcome_email(email)

        return user
