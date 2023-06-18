import time

from fastapi import Depends, FastAPI
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.crud import create, delete, get_all, read, update
from app.db import SessionLocal, engine
from app.models import Base
from app.schemas import VariableSchema

app = FastAPI()

for i in range(5):
    try:
        Base.metadata.create_all(bind=engine)
        break
    except OperationalError:
        time.sleep(i + 1)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return "Hello"


@app.post("/create/{name}")
async def create_var(name: str, var: VariableSchema, db: Session = Depends(get_db)):
    return create(db, name, var.value)


@app.get("/read/{name}")
async def read_var(name: str, db: Session = Depends(get_db)):
    return read(db, name)


@app.post("/update/{name}")
async def update_var(name: str, var: VariableSchema, db: Session = Depends(get_db)):
    return update(db, name, var.value)


@app.post("/delete/{name}")
async def delete_var(name: str, db: Session = Depends(get_db)):
    return delete(db, name)


@app.get("/list")
async def list_all(db: Session = Depends(get_db)):
    return get_all(db)
