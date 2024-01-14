from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()

db = SessionLocal()


class OurBaseModel(BaseModel):
    # class Config:
    #     orm_mode = True
    class Config:
        from_attributes = True


class Todo(OurBaseModel):
    id: int
    message: str  
    status: bool


@app.get('/', response_model=list[Todo], status_code=status.HTTP_200_OK)
def getAll_Todo():
    # Get all Todos from the database
    getAllTodo = db.query(models.Todo).all()
    return getAllTodo


@app.get('/getbyid/{todo_id}', response_model=Todo, status_code=status.HTTP_200_OK)
def get_Single_Todo(todo_id: int):
    # Get a single Todo from the database by their ID
    get_Todos = db.query(models.Todo).filter(
        models.Todo.id == todo_id).first()
    if get_Todos is not None:
        return get_Todos
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")


@app.post('/addTodo', response_model=Todo, status_code=status.HTTP_201_CREATED)
def addTodo(todo: Todo):
    # Add a new Todo to the database
    newTodo = models.Todo(id=todo.id, message=todo.message,status=todo.status)
    addTodo = db.query(models.Todo).filter(
        models.Todo.id == todo.id).first()
    if addTodo is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Todo already exists")
    db.add(newTodo)
    db.commit()

    return newTodo


@app.put('/update_todo/{todo_id}', response_model=Todo, status_code=status.HTTP_202_ACCEPTED)
def update_Todo(todo_id:int, todo: Todo):
    # Update a Todo's details in the database
    find_Todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if find_Todo is not None:
        find_Todo.id = todo.id
        find_Todo.message = todo.message
        find_Todo.status = todo.status

        db.commit()
        return find_Todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")


@app.delete('/delete_todo/{todo_id}', response_model=Todo, status_code=200)
def delete_Todo(todo_id: int):
    # Delete a Todo from the database
    find_Todo = db.query(models.Todo).filter(
        models.Todo.id == todo_id).first()
    if find_Todo is not None:
        db.delete(find_Todo)
        db.commit()
        return find_Todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo not found")


# @app.get("/",status_code=200)
# def getCar_Info():
#     return {"message":"server is running"}

# @app.post("/addTodoinfi",status_code=200)
# def addTodoInfo(Todo:Todo):
#     return {
#         "id" : Todo.id,
#         "firstname" : Todo.firstname,
#         "lastname" : Todo.lastname,
#         "isMale" : Todo.isMale
#     }
