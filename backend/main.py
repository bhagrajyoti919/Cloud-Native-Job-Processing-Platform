from fastapi import FastAPI
import redis
import json
import uuid

from prometheus_client import generate_latest
from fastapi.responses import Response

from metrics import (
    API_REQUESTS,
    JOBS_SUBMITTED,
    QUEUE_SIZE
)

app = FastAPI()

redis_client = redis.Redis(host="redis", port=6379, db=0)


@app.get("/")
def home():
    API_REQUESTS.inc()
    return {"message": "Cloud Job Processing Platform Running"}


@app.post("/submit-job")
def submit_job(task: str):
    API_REQUESTS.inc()

    job_id = str(uuid.uuid4())

    job_data = {
        "id": job_id,
        "task": task
    }

    redis_client.lpush("job_queue", json.dumps(job_data))

    # metrics
    JOBS_SUBMITTED.inc()
    QUEUE_SIZE.set(redis_client.llen("job_queue"))

    return {
        "status": "Job Submitted",
        "job_id": job_id
    }


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")