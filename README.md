# Status Dashboard

Internal Flask status dashboard service.

## Features

- Flask web application
- Docker containerization
- nginx reverse proxy
- Automated installation script

## API Endpoints

### GET /

Returns HTML dashboard page.

### GET /api/status

Redirects to:

/api/v1/status

### GET /api/v1/status

Returns JSON status information.

Example:

```json
{
  "status": "ok",
  "hostname": "container-id",
  "version": "1.0.0"
}
```

### GET /api/v1/secret

Requires header:

X-API-Key

Returns 401 if missing or invalid.

## Build Docker Image

```bash
docker build -t status-dashboard .
```

## Run Container

```bash
docker run -d \
--name status-dashboard \
-p 127.0.0.1:5000:5000 \
-e API_KEY=letmein \
-e VERSION=1.0.0 \
-e PORT=5000 \
status-dashboard
```

## Full Installation

```bash
sudo API_KEY=letmein ./install.sh
```

## Verification

```bash
curl http://localhost/api/v1/status

curl -H "X-API-Key: letmein" \
http://localhost/api/v1/secret
```# acme-status-dashboard
