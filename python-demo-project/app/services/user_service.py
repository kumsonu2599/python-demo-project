from sqlalchemy.orm import Session

from app.db.models import User
from app.queue.tasks import send_welcome_email
from app.queue.connection import queue

class UserService:

```
@staticmethod
def create_user(db: Session, name: str, email: str):
    user = User(name=name, email=email)

    db.add(user)
    db.commit()
    db.refresh(user)

    queue.enqueue(send_welcome_email, email)

    return user
```
