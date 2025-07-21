from pydantic import BaseModel, Field
from typing import List

class Size(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[Size]

class ProductResponse(ProductCreate):
    id: str = Field(..., alias="_id")

class ProductIdResponse(BaseModel):
    id: str 

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]

class OrderResponse(BaseModel):
    id: str
    userId: str
    items: List[OrderItem] 