from sqlalchemy import Column, Integer, String
from app.database import Base  # Import Base from database.py

class Item(Base):
    __tablename__ = "items"  # The name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(String)
# defining a Python class that represents a table named "items" in your database — but you are not creating the table in the database yet.
#Hey! If we create tables, one of them should be called items, and it should have these columns: id, name, value