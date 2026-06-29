collections = []


def create_collection(data):
    new_collection = {
        "id": len(collections) + 1,
        "name": data.name,
        "description": data.description
    }

    collections.append(new_collection)
    return new_collection
