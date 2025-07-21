from fastapi import APIRouter, HTTPException, status, Request, Query
from typing import List
from models import OrderCreate, OrderResponse, ProductIdResponse
from bson import ObjectId

router = APIRouter()

@router.post("/orders", response_model=ProductIdResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate, request: Request):
    order_dict = order.dict()
    result = await request.app.state.mongodb["orders"].insert_one(order_dict)
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}", response_model=List[OrderResponse])
async def list_orders_for_user(
    user_id: str,
    request: Request,
    limit: int = Query(10, gt=0),
    offset: int = Query(0, ge=0)
):
    query = {"userId": user_id}
    cursor = request.app.state.mongodb["orders"].find(query).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        order["id"] = str(order["_id"])  # Convert ObjectId to string
        del order["_id"]                 # Remove the original _id field
        orders.append(order)
    return orders 