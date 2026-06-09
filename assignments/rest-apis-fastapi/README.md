# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework in Python, practicing route creation, request/response models, and path parameters.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI App

#### Description
Set up a FastAPI application with a root GET endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Import and create a `FastAPI` app instance
- Define a `GET /` route that returns a JSON welcome message
- Run the app using `uvicorn` so it is accessible in a browser or via a client

### 🛠️ Add a POST Endpoint with a Request Body

#### Description
Define a Pydantic model and use it to accept structured data in a POST request.

#### Requirements
Completed program should:

- Define a `Pydantic` model called `Item` with `name` (str) and `price` (float) fields
- Create a `POST /items` route that accepts an `Item` in the request body
- Return the received item data along with a confirmation message
- Example response:
  ```json
  { "message": "Item received", "item": { "name": "Book", "price": 12.99 } }
  ```

### 🛠️ Add Path Parameters and Error Handling

#### Description
Extend the API with a GET endpoint that retrieves an item by ID, returning an error if the item is not found.

#### Requirements
Completed program should:

- Maintain an in-memory list or dictionary of items
- Define a `GET /items/{item_id}` route that returns the item with the given ID
- Return an HTTP 404 error with a descriptive message if the item ID does not exist
- Example usage:
  ```
  GET /items/1  →  200 OK with item data
  GET /items/99 →  404 Not Found: "Item not found"
  ```
