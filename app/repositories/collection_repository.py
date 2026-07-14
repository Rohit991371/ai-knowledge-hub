from sqlalchemy.orm import session
from app.models.collection import Collection

def create(db: Session,
           collection: Collection):
    db.add(collection)
    db.commit()
    db.refresh(collection)
    return collection


def get_all(db: Session):
    return db.query(Collection).all()


def get_by_id(db: Session, collection_id: int):
    return (
        db.query(Collection)
        .filter(Collection.id == collection_id)
        .first()
    )


def update(db: Session, collection: Collection):
    db.commit()
    db.refresh(collection)
    return collection


def delete(db: Session, collection: Collection):
    db.delete(collection)
    db.commit()