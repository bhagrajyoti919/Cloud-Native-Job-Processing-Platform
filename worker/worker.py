from prometheus_client import start_http_server
import redis
import json
import time
from prometheus_client import Histogram
from metrics import (
    QUEUE_BACKLOG_PER_WORKER,
    JOBS_PROCESSED,
    ACTIVE_WORKERS,
    JOB_PROCESS_TIME,
    QUEUE_SIZE
)

redis_client = redis.Redis(host="redis", port=6379, db=0)

# expose worker metrics
start_http_server(8001)

print("Worker started...")

while True:
    job_data = redis_client.brpop("job_queue")
    if job_data:
        ACTIVE_WORKERS.inc()
        job = json.loads(job_data[1])
        with JOB_PROCESS_TIME.time():
            # simulate processing
            print("Processing job:", job["id"])
            time.sleep(2)
        JOBS_PROCESSED.inc()
        ACTIVE_WORKERS.dec()
        queue_length = redis_client.llen("job_queue")
        QUEUE_SIZE.set(queue_length)
        workers = max(ACTIVE_WORKERS._value.get(), 1)
        QUEUE_BACKLOG_PER_WORKER.set(queue_length / workers)
