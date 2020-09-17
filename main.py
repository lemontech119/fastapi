from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
class Book(BaseModel):
    name: str
    author: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

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