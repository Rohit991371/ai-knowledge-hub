from sqlalchemy.orm import Session
from app.models.collection import Collection
from app.schemas.schema import CollectionCreate

collections = []

# def create_collection(data):
#     new_collection = {
#         "id": len(collections) + 1,
#         "name": data.name,
#         "description": data.description
#     }

#     collections.append(new_collection)
#     return new_collection


def create_collection(db: Session, collection: CollectionCreate, user_id: int):
    # 1. Instantiate the ORM model using data from schema and the authenticated user
    db_collection = Collection(
        name = collection.name,
        description = collection.description,
        user_id=user_id
    )
    
    # 2. Add, commit, and refresh using the checklist steps
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection
