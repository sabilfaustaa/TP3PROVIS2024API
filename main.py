from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Buat instance FastAPI
app = FastAPI()

# Tambahkan CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definisikan model data produk
class Product(BaseModel):
    id: int
    title: str
    price: str
    category: str
    rating: float
    reviews: int
    image: str

# Data dummy produk
products_data = [
    {
        "id": 1,
        "title": "Essentials Men's Short-Sleeve Crewneck T-Shirt",
        "price": "12.00",
        "category": "Shirt",
        "rating": 4.9,
        "reviews": 2356,
        "image": "https://respiro.co.id/cdn/shop/files/HAVANA-ProductCover-01.jpg?v=1683217282",
    },
    {
        "id": 2,
        "title": "Essentials Men's Short-Sleeve Crewneck T-Shirt",
        "price": "18.00",
        "category": "Shirt",
        "rating": 4.9,
        "reviews": 2356,
        "image": "https://respiro.co.id/cdn/shop/files/HAVANA-ProductCover-01.jpg?v=1683217282",
    },
    {
        "id": 3,
        "title": "Product 3",
        "price": "20.00",
        "category": "Shoes",
        "rating": 4.8,
        "reviews": 1234,
        "image": "https://respiro.co.id/cdn/shop/files/HAVANA-ProductCover-01.jpg?v=1683217282",
    },
    {
        "id": 4,
        "title": "Product 4",
        "price": "35.00",
        "category": "Accessories",
        "rating": 4.7,
        "reviews": 789,
        "image": "https://respiro.co.id/cdn/shop/files/HAVANA-ProductCover-01.jpg?v=1683217282",
    },
    {
        "id": 5,
        "title": "Product 5",
        "price": "25.00",
        "category": "Bag",
        "rating": 4.5,
        "reviews": 1500,
        "image": "https://respiro.co.id/cdn/shop/files/HAVANA-ProductCover-01.jpg?v=1683217282",
    },
]

@app.get("/products", response_model=List[Product])
async def get_products():
    return products_data

@app.get("/products/{product_id}", response_model=Product)
async def get_product_detail(product_id: int):
    for product in products_data:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Jalankan aplikasi FastAPI ini dengan: uvicorn <nama_file>:app --reload
