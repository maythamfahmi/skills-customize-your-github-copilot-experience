from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# TODO: Task 3 - maintain an in-memory store of items
items = {}


# TODO: Task 1 - define a GET / route that returns a welcome message
@app.get("/")
def root():
    pass


# TODO: Task 2 - define a Pydantic model called Item with name and price fields
class Item(BaseModel):
    pass


# TODO: Task 2 - define a POST /items route that accepts an Item and returns it with a confirmation message
@app.post("/items")
def create_item(item: Item):
    pass


# TODO: Task 3 - define a GET /items/{item_id} route that returns the item or raises a 404 error
@app.get("/items/{item_id}")
def get_item(item_id: int):
    pass


# Run with: uvicorn starter-code:app --reload
