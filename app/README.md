# Crud App 

This is a simple Appliction using Restful with FastAPI, PostgreSQL and SqlAlchemy ORM

## Files

### `model.py`

This file contains the SQLAlchemy model for a `Person` and a function `create_tables()` to create all tables in the database.

### `create_db.py`

This file imports the `models` module and calls the `create_tables()` function to create all tables in the database.

### `database.py`

This file sets up the SQLAlchemy engine, base class for SQLAlchemy models, and the SQLAlchemy session factory.

### `main.py`

This file contains the FastAPI application and all its routes. It uses the `Person` model from the `models` module and the session factory from the `database` module to interact with the database.

## API Endpoints

- `GET /`: Returns a list of all persons in the database.
- `GET /getbyid/{person_id}`: Returns a single person from the database by their ID.
- `POST /addperson`: Adds a new person to the database.
- `PUT /update_person/{person_id}`: Updates a person's details in the database.
- `DELETE /delete_person/{person_id}`: Deletes a person from the database.

## How to Run

1. Install all dependencies.
2. Run `python create_db.py` to create all tables in the database.
3. Run `python main.py` to start the FastAPI application.
