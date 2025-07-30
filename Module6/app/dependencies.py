from app.database import SessionLocal
def get_db():
    db = SessionLocal()  # Create a new session
    try:
        yield db  # Yield the session to be used in the request
    finally:
        db.close()  # Close the session after use