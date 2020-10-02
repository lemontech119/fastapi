from typing import Optional
from pydantic import BaseModel, EmailStr
from fastapi import FastAPI, Header


app = FastAPI()


class Book(BaseModel):
    name: str
    author: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/books/{book_id}")
def search_book(book_id: int):
    return {"book_id": book_id}


@app.post("/books/")
def create_book(book: Book):
    return book


@app.get("/headers/")
def headers(headers_test: Optional[str] = Header(None, convert_underscores=False)):
    return {"headers_test": headers_test}

