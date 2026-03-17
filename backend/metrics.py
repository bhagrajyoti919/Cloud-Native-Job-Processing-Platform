from prometheus_client import Counter, Gauge, Histogram

# API request counter
API_REQUESTS = Counter(
    "api_requests_total",
    "Total API requests"
)

# Jobs submitted
JOBS_SUBMITTED = Counter(
    "jobs_submitted_total",
    "Total jobs submitted"
)

# Jobs processed
JOBS_PROCESSED = Counter(
    "jobs_processed_total",
    "Total jobs processed"
)

# Queue size
QUEUE_SIZE = Gauge(
    "queue_size",
    "Current job queue size"
)

# Active workers
ACTIVE_WORKERS = Gauge(
    "active_workers",
    "Number of active workers"
)

# Job processing time
JOB_PROCESS_TIME = Histogram(
    "job_processing_seconds",
    "Time spent processing job"
)

QUEUE_BACKLOG_PER_WORKER = Gauge(
    "queue_backlog_per_worker",
    "Queue backlog per worker"
)