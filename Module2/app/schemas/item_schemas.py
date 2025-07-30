#schemas folder holds data models that describe the shape of data your app works with 
#pydantic is a library that helps you define and validate data structures in Python.(CHECK DATA , MAKE SURE ITS CORRECT)
#Basemodel shape of data 
from pydantic import BaseModel

class ItemSchema(BaseModel):
    id: int
    name: str
    value: float

    #It tells your app: "An item has an id (int), name (str), and value (float)" — and checks that data matches this.