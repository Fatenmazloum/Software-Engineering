🎉 Database Migration
Definition: Moving or changing the structure of a database.

Examples:

Adding a new column to a table.

Renaming , adding or deleting a table.

Moving data from one database system (e.g., MySQL) to another (e.g., PostgreSQL).

Alembic migrations change your database schema (like adding tables or columns) without deleting your data or recreating the whole database.

You can safely update your database structure as your models change.
Existing data is preserved unless your migration specifically drops or alters tables/columns in a destructive way.
This is the main advantage of using Alembic for database migrations in production projects.
Summary:
Alembic lets you evolve your database schema over time without losing important information.

pip install alembic
# Initialize Alembic

To set up Alembic in your project, run:

```bash
alembic init alembic
```

This creates an `alembic` directory and a configuration file.

# Run Alembic Migrations

After making changes to your models or database schema:

```bash
alembic revision --autogenerate -m "Add Describe your change"

"""Creates a new migration file by comparing your models to the current database.
--autogenerate tells Alembic to detect changes automatically. -m Add Describe your change adds a message describing the migration."""

alembic upgrade head 

"""Applies the latest migration(s) to your database. head means the most recent migration (the "top" of the migration history)."""
```


🧪 Unit Test = Test one small part
Tests one function only

No database, no API

Example:
“Does this add() function give the right answer?”

🔗 Integration Test = Test how parts work together
Tests many things together

Includes API, database, or services

Example:
“When I call the API, does it talk to the database and give the right result?”


200	OK	Request was successful
400	Bad Request	You gave bad input (missing or wrong format)
500	Internal Error	Something broke inside the server

To push :
git init
git add .gitignore
git add. 
git status
git commit -m "add all folders"
git branch -M main
git remote add origin ........
git push -u origin main