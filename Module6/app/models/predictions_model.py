from sqlalchemy import Column, Integer, String
from app.database import Base  # Import Base from database.py

class Predictions(Base):
    __tablename__ = "predictions"  # The name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    prediction = Column(String,index=True)