from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
load_dotenv()  # Load environment variables from .env file
DATABASE_URL = os.getenv("DATABASE_URL")#secret information like database credentials
print("DATABASE_URL from .env:", DATABASE_URL)
if not DATABASE_URL:
    raise ValueError("DATABASE_URL not found. Did you forget to create the .env file?")


#sqlalchemy is an ORM (Object Relational Mapper) that allows us to interact with the database using Python objects
#ORM mapping python classes to database tables
#Migration is the process of changing the database schema over time in a consistent and easy way(i want to edit something in database instead of dropping it if user already is using it)
#postgresql://user_name:password@server_name/dbname
#psql is postgreSQL's command line tool to connect with database
#psql postgres where postgres is the name of the database I have created
#psql -U postgres -d postgres
#postgres=# CREATE ROLE course_role WITH LOGIN PASSWORD 'mypassword';  this creates new user named course_role with password mypassword inside database named postgres
#postgres=# ALTER ROLE course_role CREATEDB; It gives the course_role user permission to create new databases other than default DB named postgres
#postgres=# CREATE DATABASE myappdb OWNER course_role; create a new database named myappdb with course_role (user) as the owner
#postgres=# GRANT ALL PRIVILEGES ON DATABASE myappdb TO course_role; gives the user full access to DB.
#\q to exit database

engine=create_engine(DATABASE_URL, echo=True)  # echo=True for SQL query logging
#connection btw python code and database; connecton to postgresql
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# A Session is how you talk to the database: add, update, query, and delete data. Build sessions
Base = declarative_base()  # Prepares SQLAlchemy to let you define tables using Python classes
#class User(Base) class  it creates a table in your database named user with columns id, name, email, and password for example