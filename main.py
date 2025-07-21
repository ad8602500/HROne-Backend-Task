from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from products import router as products_router
from orders import router as orders_router
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# MongoDB connection settings (update with your MongoDB URI)
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "hrone_ecommerce")

@app.on_event("startup")
async def startup_db_client():
    app.state.mongodb_client = AsyncIOMotorClient(MONGODB_URI)
    app.state.mongodb = app.state.mongodb_client[DB_NAME]
    await app.state.mongodb.test.insert_one({"status": "connected"})
    print("MongoDB is connected and test data inserted.")


@app.on_event("shutdown")
async def shutdown_db_client():
    app.state.mongodb_client.close()
    print("MongoDB connection closed.")

app.include_router(products_router)
app.include_router(orders_router)

@app.get("/")
async def root():
    return {"message": "HROne Backend FastAPI is running!"} 