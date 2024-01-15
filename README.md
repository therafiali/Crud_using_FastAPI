# Crud App 

This is a simple Appliction using Restful with FastAPI, PostgreSQL and SqlAlchemy ORM

## Files

### `model.py`

This file contains the SQLAlchemy model for a `Todo` and a function `create_tables()` to create all tables in the database.

### `create_db.py`

This file imports the `models` module and calls the `create_tables()` function to create all tables in the database.

### `database.py`

This file sets up the SQLAlchemy engine, base class for SQLAlchemy models, and the SQLAlchemy session factory.

### `main.py`

This file contains the FastAPI application and all its routes. It uses the `Todo` model from the `models` module and the session factory from the `database` module to interact with the database.

## API Endpoints

- `GET /`: Returns a list of all Todos in the database.
- `GET /getbyid/{Todo_id}`: Returns a single Todo from the database by their ID.
- `POST /addTodo`: Adds a new Todo to the database.
- `PUT /update_Todo/{Todo_id}`: Updates a Todo's details in the database.
- `DELETE /delete_Todo/{Todo_id}`: Deletes a Todo from the database.

## How to Run

1. Install all dependencies from `requirements.txt` file.
2. Run `python create_db.py` to create all tables in the database.
3. Run `unicorn main:app --reload` to start the FastAPI application.
4. Run `streamlit run streamlit_client.py` to start the Streamlit application.


### Connect with me
<a href="https://www.linkedin.com/in/therafiali/"><img  alt="LinkedIn" title="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0b5fbb?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
### [Directly Contact with me on email](mailto:therafiali@gmial.com)
- therafiali@gmail.com
