from sqlalchemy.orm import Session
from app.models.collection import Collection
from app.repositories import collection_repository
from app.schemas.schema import (
    CollectionCreate,
    CollectionUpdate,
)
from fastapi import HTTPException

# collections = []

# def create_collection(data):
#     new_collection = {
#         "id": len(collections) + 1,
#         "name": data.name,
#         "description": data.description
#     }

#     collections.append(new_collection)
#     return new_collection


def create_collection(db: Session,
                      collection: CollectionCreate, 
                      user_id: int
):
    # 1. Instantiate the ORM model using data from schema and the authenticated user
    db_collection = Collection(
        name = collection.name,
        description = collection.description,
        user_id=user_id
    )
    
    # 2. Add, commit, and refresh using the checklist steps
    # db.add(db_collection)
    # db.commit()
    # db.refresh(db_collection)
    
    # return db_collection
    return collection_repository.create(
        db,
        db_collection
    )


def get_all_collections(db: Session):
    # return db.query(Collection).all()  # Only business/data access - no fastapi, no router, no HTTP
    return collection_repository.get_all(db)


def get_collection_by_id(
    db: Session,
    collection_id: int
):
    # collection = (
    #     db.query(Collection)
    #     .filter(Collection.id == collection_id)
    #     .first()
    # )
    collection = collection_repository.get_by_id(
        db,
        collection_id
    )
    
    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )
        
    return collection


def update_collection(
    db: Session,
    collection_id: int,
    collection_update: CollectionUpdate
):
    # db_collection = get_collection_by_id(
    #     db,
    #     collection_id
    # )
    collection = collection_repository.get_by_id(
        db,
        collection_id
    )
    
    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )
    
    update_data = collection_update.model_dump(
        exclude_unset=True
    )
    
    for key, value in update_data.items():
        setattr(collection, key, value)
    
    # db.commit()
    # db.refresh(db_collection)
    
    # return db_collection
    return collection_repository.update(
        db,
        collection
    )


def delete_collection(
    db: Session,
    collection_id: int
):
    # collection = get_collection_by_id(
    #     db,
    #     collection_id
    # )
    collection = collection_repository.get_by_id(
        db,
        collection_id
    )
    
    if not collection:
        raise HTTPException(
            status_code=404,
            detail="Collection not found"
        )
    
    # db.delete(collection)
    # db.commit()
    
    # return {
    #     "message": f"Successfully deleted '{collection.name}' "
    # }
    collection_repository.delete(
        db,
        collection
    )
    return {
        "message": f"Successfully deleted '{collection.name}'"
    }