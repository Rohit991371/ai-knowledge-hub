from app.database import Base, engine

#Import all models so SQLAlchemy knows about them
from app.models.user import User
from app.models.collection import Collection
from app.models.document import Document

def init_db():
    Base.metadata.create_all(bind=engine)