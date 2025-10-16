from fastapi import FastAPI, HTTPException  # type: ignore
from pydantic import BaseModel  # type: ignore

# command line to run uvicorn uvicorn main:app --reload
app = FastAPI()


class Item(BaseModel):
    text: str = None
    # if removed the str = None, it will make it a required
    is_done: bool = False


items = []


@app.get("/")
def root():
    return {"Hello": "World"}


@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return items


@app.get("/items")
def list_items(limit: int = 10):
    return items[0:limit]


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found",
        )

#  http://127.0.0.1:8000/docs#/
#  http://127.0.0.1:8000/redocs
#  comment above really important
