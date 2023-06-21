# DevOps Project

## Prerequisites

- K3d

## Running

- `k3d cluster delete cl`
- `k3d cluster create cl -p "8081:80@loadbalancer"`
- `cd kubernetes`
- `kubectl apply -f namespace.yaml -f deployment.yaml -f service.yaml -f ingress.yaml -f database.yaml`
