# Books CRUD App - DevOps Project

## Prerequisites

- Docker
- K3d

If you are running outside Docker and Kubernetes, you need:

- Python 3.10
- Poetry
- PostgreSQL

## Running (Normal)

- `poetry install`
- Create a `.env` file with the environment variables `POSTGRES_URL`, `POSTGRES_DATABASE`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
- `uvicorn app.main:app`

## Running (Docker)

- Create a `.env` file with the environment variables `POSTGRES_URL`, `POSTGRES_DATABASE`, `POSTGRES_USER`, `POSTGRES_PASSWORD`
- `docker compose up`

## Running (Kubernetes)

- `k3d cluster create cl -p "8081:80@loadbalancer"`
- `cd kubernetes`
- `kubectl apply -f namespace.yaml -f deployment.yaml -f service.yaml -f ingress.yaml -f database.yaml` - the order of the manifests matters
