from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from database import SessionLocal
import models

app = FastAPI()

db = SessionLocal()


class OurBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Person(OurBaseModel):
    id: int
    firstname: str
    lastname: str
    isMale: bool


@app.get('/', response_model=list[Person], status_code=status.HTTP_200_OK)
def getAll_Person(person: Person):
    # Get all persons from the database
    getAllPerson = db.query(models.Person).all()
    return getAllPerson


@app.get('/getbyid/{person_id}', response_model=Person, status_code=status.HTTP_200_OK)
def get_Single_Person(person_id: int):
    # Get a single person from the database by their ID
    get_persons = db.query(models.Person).filter(
        models.Person.id == person_id).first()
    if get_persons is not None:
        return get_persons
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Person not found")


@app.post('/addperson', response_model=Person, status_code=status.HTTP_201_CREATED)
def addPerson(person: Person):
    # Add a new person to the database
    newPerson = models.Person(id=person.id, firstname=person.firstname,
                              lastname=person.lastname, isMale=person.isMale)
    addPerson = db.query(models.Person).filter(
        models.Person.id == person.id).first()
    if addPerson is not None:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Person already exists")
    db.add(newPerson)
    db.commit()

    return newPerson


@app.put('/update_person/{person_id}', response_model=Person, status_code=status.HTTP_202_ACCEPTED)
def update_person(person_id: int, person: Person):
    # Update a person's details in the database
    find_person = db.query(models.Person).filter(
        models.Person.id == person_id).first()
    if find_person is not None:
        find_person.id = person.id
        find_person.firstname = person.firstname
        find_person.lastname = person.lastname
        find_person.isMale = person.isMale

        db.commit()
        return find_person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Person not found")


@app.delete('/delete_person/{person_id}', response_model=Person, status_code=200)
def delete_person(person_id: int):
    # Delete a person from the database
    find_person = db.query(models.Person).filter(
        models.Person.id == person_id).first()
    if find_person is not None:
        db.delete(find_person)
        db.commit()
        return find_person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail="Person not found")


# @app.get("/",status_code=200)
# def getCar_Info():
#     return {"message":"server is running"}

# @app.post("/addpersoninfi",status_code=200)
# def addPersonInfo(person:Person):
#     return {
#         "id" : person.id,
#         "firstname" : person.firstname,
#         "lastname" : person.lastname,
#         "isMale" : person.isMale
#     }
