# Cloud-Native Job Processing Platform

A scalable, cloud-native job processing system built with FastAPI, Redis, and Docker, designed for high availability and observability using Prometheus and Grafana, and deployable on Kubernetes.

## 🚀 Overview

This platform provides a robust architecture for submitting and processing background jobs. It uses a producer-consumer pattern where a backend API (FastAPI) submits jobs to a Redis queue, and multiple worker instances consume and process these jobs. The system is fully containerized and includes comprehensive monitoring and auto-scaling capabilities.

## 🛠 Architecture

- **Backend API (FastAPI)**: Handles job submissions and exposes Prometheus metrics.
- **Message Broker (Redis)**: Acts as a reliable task queue.
- **Worker Service (Python)**: Processes jobs from the queue and reports performance metrics.
- **Monitoring (Prometheus & Grafana)**: Collects and visualizes system health, queue size, and processing latency.
- **Orchestration (Kubernetes)**: Manages deployments, services, and Horizontal Pod Autoscaling (HPA).

## 📁 Project Structure

- `backend/`: FastAPI application code and Prometheus metrics definitions.
- `worker/`: Background worker logic for job processing.
- `kubernetes/`: K8s manifests for deployments, services, and HPA.
- `monitoring/`: Configuration for Prometheus (alerts and scrape configs).
- `ci-cd/`: Jenkins pipeline definition for automated builds and deployments.
- `docker-compose.yml`: Local development setup for the entire stack.

## 🚀 Getting Started

### Local Development (Docker Compose)

To start the entire stack locally:

```bash
docker-compose up --build
```

Access the services:
- **Backend API**: `http://localhost:8000`
- **Prometheus**: `http://localhost:9090`
- **Grafana**: `http://localhost:3000`

### Kubernetes Deployment

1. **Start your cluster** (e.g., Minikube):
   ```bash
   minikube start --driver=docker
   ```

2. **Apply manifests**:
   ```bash
   kubectl apply -f kubernetes/
   ```

3. **Install Monitoring Stack** (Helm):
   ```bash
   helm install monitoring prometheus-community/kube-prometheus-stack
   ```

## 📊 Monitoring & Metrics

The system tracks several key performance indicators (KPIs):
- `api_requests_total`: Total number of API calls.
- `jobs_submitted_total`: Number of jobs added to the queue.
- `jobs_processed_total`: Number of jobs successfully completed.
- `queue_size`: Current number of pending jobs in Redis.
- `job_process_time_seconds`: Histogram of time taken to process jobs.

## 🔄 CI/CD Pipeline

The project includes a `Jenkinsfile` that automates:
1. Building Docker images for backend and worker.
2. Pushing images to a container registry.
3. Deploying updated manifests to the Kubernetes cluster.

## 📈 Auto-scaling

The `worker-hpa.yaml` defines horizontal scaling for the worker nodes based on CPU utilization, ensuring the system can handle spikes in job submissions efficiently.
