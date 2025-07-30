from app.schemas.item_schemas import ItemSchema
from app.utils.exceptions import itemNotFoundError
from app.models.item_model import Item
from sqlalchemy.orm import Session
from app.models.item_model import Item
from app.schemas.item_schemas import ItemSchema
from app.utils.exceptions import itemNotFoundError

def create_item(item: ItemSchema, db: Session):
    db_item = Item(id=item.id, name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(item_id: int, db: Session):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise itemNotFoundError(f"Item with id {item_id} not found.")
    return db_item

def update_item(item_id: int, item: ItemSchema, db: Session):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise itemNotFoundError(f"Item with id {item_id} not found.")
    db_item.name = item.name
    db_item.value = item.value
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_item(item_id: int, db: Session):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise itemNotFoundError(f"Item with id {item_id} not found.")
    db.delete(db_item)
    db.commit()
    return db_item

def list_items(db: Session):
    return db.query(Item).all()
