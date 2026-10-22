import os

import redis
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Docker Practice API")

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=6379,
    decode_responses=True,
    socket_connect_timeout=2,
)


@app.get("/")
def home():
    return {
        "message": "My first Dockerized API",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/visits")
def visits():
    try:
        count = redis_client.incr("visit_count")
        return {"visits": count}
    except redis.RedisError as exc:
        raise HTTPException(
            status_code=503,
            detail="Redis is unavailable",
        ) from exc