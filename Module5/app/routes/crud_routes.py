#It receives the request and calls the service.
from fastapi import APIRouter, HTTPException,Depends
from app.schemas.item_schemas import ItemSchema
from app.services.crud_services import create_item, get_item, update_item, delete_item, list_items
from app.utils.exceptions import itemNotFoundError
from app.dependencies import get_db
from sqlalchemy.orm import Session

#routes are  like buttons on a website perform actions (like "Submit", "Delete", "Update")...
#Think of APIRouter like a folder where you group similar routes.
#Instead of putting all your routes in main.py, you create small groups like:
#user_routes → for user-related things
#item_routes → for items
#order_routes → for orders
#This means all routes inside will start with /items and appear under "faten" in /docs.
router = APIRouter(prefix="/items", tags=["faten"])
#post localhost:8000/items
#input and output of router item object
#This route is like a receptionist 🧑‍💻 who talks to the user (someone who sends a request to create an item),then calls the worker (the create_item function in the services) to actually do the job.

@router.post("/", response_model=ItemSchema)
#These routes receive user requests (like from Swagger UI or frontend).Each route calls the matching service function.
def create_item_route(item: ItemSchema, db: Session = Depends(get_db)):#talks to user
    try:
        return create_item(item,db)#do the work behind the scenes
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{item_id}", response_model=ItemSchema)
def get_item_route(item_id: int,db: Session = Depends(get_db)):
    try:
        return get_item(item_id,db)
    except itemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/{item_id}", response_model=ItemSchema)
def update_item_route(item_id: int, item: ItemSchema,db: Session = Depends(get_db)):      
    try:
        return update_item(item_id, item,db)
    except itemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.delete("/{item_id}")
def delete_item_route(item_id: int,db: Session = Depends(get_db)):    
    try:
        delete_item(item_id,db)
        return {"message": f"Item with id {item_id} deleted successfully."}
    except itemNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/", response_model=list[ItemSchema])
def list_items_route(db: Session = Depends(get_db)):     
    try:
        return list_items(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))