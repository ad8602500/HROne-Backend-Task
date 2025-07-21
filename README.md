# HROne Backend Task

This is a sample e-commerce backend built with FastAPI and MongoDB (using Motor) for the HROne Backend Intern Hiring Task.

## Features
- Product APIs (create, list with filters)
- Order APIs (create, list for user)
- MongoDB integration

## Tech Stack
- Python 3.10+
- FastAPI
- Motor (async MongoDB driver)
- Uvicorn (ASGI server)

## Setup Instructions

1. **Clone the repository**
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up MongoDB**
   - Use MongoDB Atlas (free tier) or local MongoDB instance.
   - Set the `MONGODB_URI` environment variable if not using the default.
4. **Run the FastAPI app**
   ```bash
   uvicorn main:app --reload
   ```
5. **API Docs**
   - Visit [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

## Environment Variables
- `MONGODB_URI`: MongoDB connection string (default: `mongodb://localhost:27017`)
- `DB_NAME`: Database name (default: `hrone_ecommerce`)

---

## To Do
- Implement Product and Order APIs as per the task requirements. 