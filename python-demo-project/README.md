# Demo Python Backend Project

## Start Services

docker-compose up -d

## Install Dependencies

pip install -r requirements.txt

## Run API

uvicorn app.main:app --reload

## Run Worker

python -m app.queue.worker
