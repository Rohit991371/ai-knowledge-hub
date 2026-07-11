from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


#    description: str | None = None
# None to make it just optional


# Request Body
class CollectionCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=100
    )
    owner: str = Field(
        min_length=2,
        max_length=50
    )
    description: str = Field(
        min_length=10,
        max_length=200,
    )


# Response Model
class CollectionResponse(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class CollectionUpdate(BaseModel):
    name: Optional[str] = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    owner: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=50
    )

    description: Optional[str] = None
