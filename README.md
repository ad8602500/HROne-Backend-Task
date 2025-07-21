# HROne Backend FastAPI

This is a backend API for an e-commerce application (like Flipkart/Amazon) built with FastAPI and MongoDB. It provides endpoints for managing products and orders, with support for filtering, pagination, and more.

---

## 🚀 Live Demo
[HROne Backend on Render](https://hrone-backend-task-t53f.onrender.com/)

---

## 📁 Project Structure

```
HROne Backend/
  └── HROne-Backend-Task/
        ├── main.py           # FastAPI app entry point
        ├── models.py         # Pydantic models for Products and Orders
        ├── products.py       # Product endpoints (CRUD, filtering, pagination)
        ├── orders.py         # Order endpoints (create, list, user orders)
        ├── requirements.txt  # Python dependencies
        └── README.md         # Project documentation
```

---

## 🛠️ Features
- **Products API**: Create, list (with filtering, pagination)
- **Orders API**: Create order, list orders for a user
- **MongoDB**: Async database access using Motor
- **Environment Variables**: Secure config with `.env` and `python-dotenv`
- **Ready for deployment**: Works on Render and similar platforms

---

## ⚙️ Environment Variables
Create a `.env` file in the root of `HROne-Backend-Task/` with:
```
MONGODB_URI=your_mongodb_connection_string
DB_NAME=your_database_name
```

---

## 🧑‍💻 Installation & Running Locally
1. **Clone the repo:**
   ```sh
   git clone <your-repo-url>
   cd HROne-Backend-Task
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file as shown above.
4. **Run the app:**
   ```sh
   uvicorn main:app --reload
   ```
5. **API Docs:**
   - Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Deployment
This project is deployed on Render:
- [https://hrone-backend-task-t53f.onrender.com/](https://hrone-backend-task-t53f.onrender.com/)

---

## 📬 API Endpoints
- `POST /products` - Create a product
- `GET /products` - List products (with filters, pagination)
- `POST /orders` - Create an order
- `GET /orders/{user_id}` - List orders for a user

See the API docs at `/docs` for full details and request/response formats.

---

## 📝 License
MIT (or specify your license) 