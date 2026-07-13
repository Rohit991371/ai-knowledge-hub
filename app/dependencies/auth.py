from typing import Generator
from app.database import SessionLocal

def get_current_user():
    return {
        "id": 1,
        "username": "rohit",
        "role": "user"
    }
