from typing import Generator
from app.database import SessionLocal

def get_current_user():
    return {
        "id": 1,
        "username": "rohit",
        "role": "user"
    }


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db  # This hands the session to router
    finally:
        db.close()
