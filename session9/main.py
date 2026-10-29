from fastapi import fastAPI

app = FastAPI()

@App.get("/")
def read_root():
    return {"message", "Hello UFV from FastAPI!"}

@App.get("/items/{id}")
def get_item(id: int):
    return{"id": id, "name": "Laptop"}