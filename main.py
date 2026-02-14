from datetime import datetime
from fastapi import FastAPI

app = FastAPI(title="Server Time API")


@app.get("/")
def root():
    """Корневой эндпоинт с приветствием."""
    return {"message": "Server Time API", "docs": "/docs", "version": "1.1"}


@app.get("/time")
def get_server_time():
    """Возвращает текущее время сервера в ISO формате и timestamp."""
    now = datetime.utcnow()
    return {
        "server_time_utc": now.isoformat() + "Z",
        "timestamp": int(now.timestamp()),
        "timezone": "UTC",
    }
