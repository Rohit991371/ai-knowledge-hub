from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.schema import CollectionCreate, CollectionResponse, CollectionUpdate
from app.services.collection_services import create_collection
from app.models.collection import Collection
from app.dependencies.auth import get_db, get_current_user

router = APIRouter()

# collections = [
#     {"id": 1, "name": "FastAPI Notes", "owner": "rohit"},
#     {"id": 2, "name": "Machine Learning", "owner": "rohit"},
#     {"id": 3, "name": "Deep Learning", "owner": "rohit"},
# ]

# Read ALL (GET /collections)


@router.get("/")
def get_collections(
    db: Session = Depends(get_db)
):
    # return collections
    return db.query(Collection).all()


# Read ONE (GET /collections/{id})
@router.get("/{collection_id}")
def get_one_collection(collection_id: int,
                       db: Session = Depends(get_db)):
    # 1. Query the DB and look for the first match
    collection = db.query(Collection).filter(
        Collection.id == collection_id).first()

    # 2. If it doesn't exist, raise the 404 error
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")

    # 3. Otherwise, return the dound database record
    return collection

    # for c in collections:
    #     if c["id"] == collection_id:
    #         return c

    # raise HTTPException(status_code=404, detail="Collection not found")


# CREATE (POST /collections)
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_collections(collection: CollectionCreate,
                       db: Session = Depends(get_db),
                       current_user=Depends(get_current_user)):

    # Pass the database session and data to the service layer
    return create_collection(db=db, collection=collection, user_id=current_user["id"])

    # new_collection = {
    #     "id": len(collections) + 1,
    #     "name": collection.name,
    #     "owner": collection.owner
    # }
    # collections.append(new_collection)
    # return new_collection


# Update (PATCH /collections/{id})
@router.patch("/{collection_id}")
def update_collection(collection_id: int,
                      collection_update: CollectionUpdate,
                      db: Session = Depends(get_db)):
    # 1. Fetch the item
    db_item = db.query(Collection).filter(
        Collection.id == collection_id).first()

    # 2. Safety Check : 404 if not found
    if not db_item:
        raise HTTPException(status_code=404, detail="Collection Not Found")

    # 3. Dynamically extract user input (excluding fields they left out)
    update_data = collection_update.model_dump(exclude_unset=True)

    # 4. Loop through the incoming data and update the database model attributes
    for key, value in update_data.items():
        setattr(db_item, key, value)

    # 5. Commit and refresh
    db.commit()
    db.refresh(db_item)
    return db_item

    # for c in collections:
    #     if c["id"] == collection_id:
    #         update_data = collection_update.model_dump(exclude_unset=True)
    #         c.update(update_data)
    #         return c

    # raise HTTPException(status_code=404, detail="Collection Not Found")


# Delete (DELETE /collections/{id})
@router.delete("/{collection_id}")
# Added missing db dependency!
def delete_collection(collection_id: int, db: Session = Depends(get_db)):
    # 1. Fetch the item
    db_item = db.query(Collection).filter(
        Collection.id == collection_id).first()

    # 2. Safety Check : 404 if not found
    if not db_item:
        raise HTTPException(status_code=404, detail="Collection not found")

    db.delete(db_item)
    db.commit()

    return {"message": f"Successfully deleted '{db_item.name}'"}

    # for index, c in enumerate(collections):
    #     if c["id"] == collection_id:
    #         deleted_item = collections.pop(index)
    #         return {"message": f"Successfully deleted '{deleted_item['name']}'"}

    # raise HTTPException(status_code=404, detail="Collection not found")
