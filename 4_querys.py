from typing import Annotated, Optional
from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from .database import get_db
from .models import Item

app = FastAPI()

@app.get("/items")
def get_items(
    db: Annotated[Session, Depends(get_db)],
    # 1. Search filter with length validation
    search: Annotated[Optional[str], Query(max_length=50, description="Search by item name")] = None,
    # 2. Pagination parameters with floor/ceiling constraints
    skip: Annotated[int, Query(ge=0, description="Number of records to skip")] = 0,
    limit: Annotated[int, Query(ge=1, le=100, description="Max records to return")] = 20,
    # 3. Categorical filter
    category: Annotated[Optional[str], Query()] = None
):
    # Construct base query
    query = db.query(Item)
    
    # Apply dynamic filters based on query params
    if search:
        query = query.filter(Item.name.ilike(f"%{search}%"))
    if category:
        query = query.filter(Item.category == category)
        
    # Execute database pagination
    total_count = query.count()
    items = query.offset(skip).limit(limit).all()
    
    return {
        "total": total_count,
        "skip": skip,
        "limit": limit,
        "data": items
    }
