from contextlib import asynccontextmanager
from fastapi import FastAPI
import logging
from app.init_db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Initializing database...")
    init_db()

    yield

    print("Application shutting down....")

app = FastAPI(
    title="AI Knowledge Hub",
    lifespan=lifespan
)


# ================================================================================

# from fastapi import FastAPI
# from enum import Enum
# from ai_knowledge_hub.app.schemas.schema import CollectionCreate, CollectionResponse, CollectionUpdate
# from fastapi import status, Response
# from fastapi import HTTPException
# from datetime import datetime, timezone

# from app.routers.collections import router as collections_router


# app = FastAPI(title="AI Knowledge Hub")


# """
# # ------------------------------ Working with Enumeration-------------------------------------
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#     gpt = "gpt"


# @app.get("/models/{model_name}")
# def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name is ModelName.resnet:
#         return {"model_name": model_name, "message": "Have some residuals"}

#     if model_name is ModelName.lenet:
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Generative Pretrained Transformer"}


# # -------------------------------------------------------------------
# @app.get("/")
# def root():
#     return {
#         "message": "Welcome to the AI Knowledge Hub!"
#     }


# @app.get("/health")
# def health_check():
#     return {
#         "status": "healthy"
#     }


# @app.get("/about")
# def about():
#     return {
#         "project": "AI Knowledge Hub",
#         "version": "1.0.0",
#     }


# @app.get("/api-info")
# def api_info():
#     return {
#         "name": "AI Knowledge Hub API",
#         "docs": "/docs"
#     }


# collections = [
#     {
#         "id": 1,
#         "name": "FastAPI Notes"
#     },
#     {
#         "id": 2,
#         "name": "AI Research Papers"
#     },
#     {
#         "id": 3,
#         "name": "Machine Learning Tutorials"
#     },
#     {
#         "id": 4,
#         "name": "FastAPI Learning",
#         "Documents": 24,
#         "stats": [
#             {
#                 "id": 4.1,
#                 "health_check": "healthy"
#             }
#         ]
#     }
# ]


# @app.get("/collections")
# def get_collections():
#     return collections


# @app.get("/collections/{collection_id}")
# def get_collection(collection_id: int):
#     for collection in collections:
#         if collection["id"] == collection_id:
#             return collection

#     return {
#         "error": "Collection not found."
#     }

# # ------------------------------Path Convertor-------------------------------------
# # /files/{file_path:path}


# @app.get("/documents/{file_path:path}")
# def read_document(file_path: str):
#     return {
#         "action": "reading file",
#         "requested_file_path": file_path,
#         "message": f"Returning contents of '{file_path}' right here!"
#     }


# queryParam_collections = [
#     {"id": 1, "name": "FastAPI Notes", "owner": "rohit"},
#     {"id": 2, "name": "Machine Learning", "owner": "rohit"},
#     {"id": 3, "name": "Deep Learning", "owner": "rohit"},
#     {"id": 4, "name": "Neural Network", "owner": "rohit"},
#     {"id": 5, "name": "Embeddings", "owner": "rohit"},
#     {"id": 6, "name": "NLP", "owner": "rohit"},
#     {"id": 7, "name": "Tokenization", "owner": "rohit"},
#     {"id": 8, "name": "Learning FastAPI", "owner": "rohit"},
#     {"id": 9, "name": "Backend Notes", "owner": "rohit"},
#     {"id": 10, "name": "ML", "owner": "alice"}
# ]


# # Query Parameter
# @app.get("/queryParam_collections")
# def get_queryParam_collections(
#         limit: int = 10):
#     return queryParam_collections[:limit]


# # Multiple Query Parameters
# @app.get("/queryParam_collections2")
# def get_queryParam_collections2(
#     limit: int = 10,
#     skip: int = 2
# ):
#     return queryParam_collections[skip:skip+limit]


# # Search Functionality
# @app.get("/search_query")
# def get_search_query(
#     search: str | None = None
# ):
#     if search:
#         return [
#             collection
#             for collection in queryParam_collections
#             if search.lower()
#             in collection["name"].lower()
#         ]

#     return queryParam_collections


# @app.get("/combined_collections")
# def get_combined(
#     search: str | None = None,
#     limit: int = 10,
#     skip: int = 0
# ):
#     filtered = queryParam_collections
#     if search:
#         filtered = [
#             c for c in filtered
#             if search.lower() in c["name"].lower()
#         ]

#     return filtered[skip:skip+limit]


# @app.get("/owner")
# def get_owner(
#     search: str | None = None,
#     limit: int = 10,
#     skip: int = 0
# ):
#     filtered = queryParam_collections
#     if search:
#         filtered = [
#             c for c in filtered
#             if search.lower() in c["owner"].lower()
#         ]

#     return filtered[skip:skip+limit]


# @app.get("/combined_collections2")
# def get_combined(
#     name: str | None = None,
#     owner: str | None = None,
#     limit: int = 10,
#     skip: int = 0
# ):
#     filtered = queryParam_collections
#     if name:
#         filtered = [
#             c for c in filtered
#             if name.lower() in c["name"].lower()
#         ]

#     if owner:
#         filtered = [
#             c for c in filtered
#             if owner.lower() in c["owner"].lower()
#         ]

#     return filtered[skip:skip+limit]


# # Query parameter type conversion
# @app.get("/summary")
# def get_summary(short: bool = False):
#     # if user sets short=true, give the brief version
#     if short:
#         return {"message": "AI is Cool"}
#     # otherwise, give them the long version
#     return {
#         "message": "Artificial Intelligence is a vast field encompassing machine learning"
#     }


# # Multiple Path and Query Parameters
# @app.get("/owner/{id}/queryParam_collections")
# def get_user_collections(
#     id: int,
#     search: str | None = None,
#     name: str | None = None,
#     owner: str | None = None,
# ):
#     return {
#         "action": "fetching collections",
#         "user": id,
#         "search_applied": search,
#         "message": f"Fetching documents for user {id}. Searching for: {search}",
#         "found": f"owner: {owner} and name: {name}"
#     }


# post_collection = []


# @app.post("/post_collection", response_model=CollectionResponse)
# def create_collection(collection: CollectionCreate):
#     new_post_collection = {
#         "id": len(post_collection) + 1,
#         "name": collection.name,
#         "owner": collection.owner,
#         "description": collection.description,
#         "count": len(collection.description)
#     }

#     post_collection.append(new_post_collection)

#     return new_post_collection


# # Lesson 1.4 - Proper Error Handling and HTTP Exceptions

# # This will behave like helper
# def find_collection(collection_id: int):
#     for collection in queryParam_collections:
#         if collection["id"] == collection_id:
#             return collection

#     raise HTTPException(
#         status_code=404,
#         detail="Collection not found"
#     )


# @app.get("/queryParam_collections/{collection_id}")
# def get_collection(collection_id: int):
#     return find_collection(collection_id)
# # def get_collection(collection_id: int):
# #     for collection in queryParam_collections:
# #         if collection["id"] == collection_id:
# #             return collection

# #     raise HTTPException(
# #         status_code=404,
# #         detail="Collection not found"
# #     )


# # @app.delete("/queryParam_collections/{collection_id}", status_code=status.HTTP_204_NO_CONTENT)
# # def delete_collection(collection_id: int):
# #     # search for the collection_id
# #     for index, collection in enumerate(queryParam_collections):
# #         if collection["id"] == collection_id:
# #             del queryParam_collections[index]
# #             return

# #     raise HTTPException(
# #         status_code=status.HTTP_404_NOT_FOUND,
# #         detail="Item not found"
# #     )


# @app.patch("/queryParam_collections/{collection_id}")
# def update_collection(
#     collection_id: int,
#     collection_update: CollectionUpdate,
# ):

#     collection = find_collection(collection_id)
#     if not collection:
#         return {"error": "Collection not found"}

#     update_data = collection_update.model_dump(
#         exclude_unset=True
#     )

#     # Timestamp righ now during execution
#     current_time = datetime.now(timezone.utc).isoformat()

#     # inject the timestamp into our update dictionary
#     update_data["updated_at"] = current_time

#     collection.update(update_data)

#     return collection


# @app.delete(
#     "/queryParam_collections/{collection_id}",
#     status_code=status.HTTP_204_NO_CONTENT
# )
# def delete_collection(collection_id: int):
#     collection = find_collection(collection_id)
#     queryParam_collections.remove(collection)

#     return Response(
#         status_code=status.HTTP_204_NO_CONTENT
#     )
# """

# # ------------------------------------------------
# app.include_router(
#     collections_router,
#     prefix="/collections",
#     tags=["Collections"]
# )
