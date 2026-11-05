from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

# 1. Define the schema/structure of the incoming data using Pydantic
class Item(BaseModel):
    name: str = Field(..., description="The name of the product", example="Wireless Mouse")
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    is_offer: Optional[bool] = None
    tax: Optional[float] = None

# 2. Create the POST endpoint that accepts the Request Body
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item, q: Optional[str] = None):
    # Calculate final price if tax is provided
    total_price = item.price
    if item.tax:
        total_price += item.tax

    # Return a combined response containing Path, Query, and Body data
    return {
        "message": "Item processed successfully",
        "item_id": item_id,
        "query_param": q,
        "received_data": item.dict(),
        "calculated_total_price": total_price
    }
