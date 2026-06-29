from fastapi import APIRouter, HTTPException, status, Depends
from ai_knowledge_hub.app.schemas.schema import CollectionCreate, CollectionResponse, CollectionUpdate
from app.services.collection_services import create_collection
from app.dependencies.auth import get_current_user

router = APIRouter()

collections = [
    {"id": 1, "name": "FastAPI Notes", "owner": "rohit"},
    {"id": 2, "name": "Machine Learning", "owner": "rohit"},
    {"id": 3, "name": "Deep Learning", "owner": "rohit"},
]

# Read ALL (GET /collections)
@router.get("/")
def get_collections():
    return collections

# Read ONE (GET /collections/{id})
@router.get("/{collection_id}")
def get_one_collection(collection_id: int):
    for c in collections:
        if c["id"] == collection_id:
            return c

    raise HTTPException(status_code=404, detail="Collection not found")

# CREATE (POST /collections)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_collections(collection: CollectionCreate,
                       current_user=Depends(get_current_user)):
    new_collection = {
        "id": len(collections) + 1,
        "name": collection.name,
        "owner": collection.owner
    }
    collections.append(new_collection)
    return new_collection


# Update (PATCH /collections/{id})
@router.patch("/{collection_id}")
def update_collection(collection_id: int, collection_update: CollectionUpdate):
    for c in collections:
        if c["id"] == collection_id:
            update_data = collection_update.model_dump(exclude_unset=True)
            c.update(update_data)
            return c

    raise HTTPException(status_code=404, detail="Collection Not Found")


# Delete (DELETE /collections/{id})
@router.delete("/{collection_id}")
def delete_collection(collection_id: int):
    for index, c in enumerate(collections):
        if c["id"] == collection_id:
            deleted_item = collections.pop(index)
            return {"message": f"Successfully deleted '{deleted_item['name']}'"}

    raise HTTPException(status_code=404, detail="Collection not found")

