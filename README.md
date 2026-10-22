# Docker Learn

A small FastAPI project for practicing Docker and Docker Compose. The API is in
`app/main.py`, and `docker-compose.yml` defines the API and a PostgreSQL
container.

## Run with Docker Compose

```sh
docker compose up --build
```

The API is available at <http://localhost:8000>. Interactive API docs are at
<http://localhost:8000/docs>.

## Endpoints

- `GET /` - basic API status
- `GET /health` - health check
- `GET /visits` - increments and returns a Redis-backed visit count

The current Compose configuration does not start Redis, so `/visits` returns
`503` unless Redis is made available and configured for the app. The PostgreSQL
container is defined in Compose but is not currently used by the API.

## Run locally

Requires Python 3.12 or later and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
uv run uvicorn app.main:app --reload --port 8000
```
