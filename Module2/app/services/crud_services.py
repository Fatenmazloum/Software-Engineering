from app.schemas.item_schemas import ItemSchema
from app.utils.exceptions import itemNotFoundError
"""
This is a dictionary called db that will store items.

Keys are integers (int), representing the item’s id.

Values are of type ItemSchema (probably a class/model).
"""
db: dict[int, ItemSchema] = {}
def create_item(item: ItemSchema):
    db[item.id] = item
    return item

def get_item(item_id: int):
    if item_id not in db:
        raise itemNotFoundError(f"Item with id {item_id} not found.")
    return db[item_id]

def update_item(item_id: int, item: ItemSchema):
    if item_id not in db:
        raise itemNotFoundError(f"Item with id {item_id} not found.")
    db[item_id] = item
    return item

def delete_item(item_id: int):
    if item_id not in db:
        raise itemNotFoundError(f"Item with id {item_id} not found.")
    return db.pop(item_id)

def list_items():
    return list(db.values())

"""
services/ → Logic layer (the brain 🧠) works behind the scene
This folder contains functions that do the real work, like:

Talking to the database

Doing calculations

Calling models

Business rules (what to do, how, and when)
"""



    



