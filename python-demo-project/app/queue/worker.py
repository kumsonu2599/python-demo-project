from redis import Redis
from rq import Worker
from rq import Queue
from rq import Connection

from app.core.config import settings

redis_conn = Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT
)

queue = Queue(connection=redis_conn)


if __name__ == "__main__":
    with Connection(redis_conn):
        worker = Worker([queue])
        worker.work()
