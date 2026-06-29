from lib import books
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import utils

app = FastAPI(
    title="Library API",
    description="API quản lý sách thư viện",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def get_health():
    return {"message": "Library API is running"}


@app.get("/books")
def get_books():
    return {
        "status": "success",
        "message": "Get books successfully",
        "data": books
    }


@app.get("/books/available")
def get_books_available():
    available_books = utils.get_return_book(books, is_available=True)

    return {
        "status": "success",
        "message": "Get available books successfully",
        "data": available_books
    }


@app.get("/books/borrowed")
def get_books_borrowed():
    borrowed_books = utils.get_return_book(books, is_available=False)

    return {
        "status": "success",
        "message": "Get borrowed books successfully",
        "data": borrowed_books
    }