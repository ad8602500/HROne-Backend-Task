from fastapi import APIRouter, status, Request, Query
from typing import List, Optional
from models import ProductCreate, ProductIdResponse
from bson import ObjectId

router = APIRouter()

@router.post("/products", response_model=ProductIdResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate, request: Request):
    product_dict = product.dict()
    result = await request.app.state.mongodb["products"].insert_one(product_dict)
    return {"id": str(result.inserted_id)}

@router.get("/products")
async def list_products(
    request: Request,
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: int = Query(10, gt=0),
    offset: int = Query(0, ge=0)
):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["sizes.size"] = size
    cursor = request.app.state.mongodb["products"].find(query).skip(offset).limit(limit)
    products = []
    async for product in cursor:
        products.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "price": product["price"]
        })
    page = {
        "next": offset + limit,
        "limit": len(products),
        "previous": max(offset - limit, 0)
    }
    return {"data": products, "page": page} 