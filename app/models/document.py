from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id = Column(Integer, primary_key=True, index=True)
    
    filename = Column(String(255), nullable=False)
    
    filepath = Column(String(500), nullable=False)
    
    file_size = Column(Integer, nullable=False)
    
    collection_id = Column(
        Integer,
        ForeignKey("collections.id"),
        nullable=False
    )
    
    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    
    collection = relationship(
        "Collection",
        back_populates="documents"
    )