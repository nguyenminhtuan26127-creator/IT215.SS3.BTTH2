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


@app.get("/books/statistics")
def get_book_statistics():
    total_books = len(books)
    available_books = len(utils.get_return_book(books, is_available=True))
    borrowed_books = len(utils.get_return_book(books, is_available=False))

    return {
        "status": "success",
        "message": "Get statistics book successfully",
        "data": {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books
        }
    }


@app.get("/books/categories")
def get_book_categories():
    # Dùng sorted() để thứ tự trả về nhất quán, không bị random mỗi lần gọi
    categories = sorted(set(book["category"] for book in books))

    return {
        "status": "success",
        "message": "Get categories successfully",
        "data": categories
    }


@app.get("/books/latest")
def get_book_latest():
    # Guard: tránh lỗi khi danh sách sách rỗng
    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    latest_book = max(books, key=lambda book: book["year"])

    return {
        "status": "success",
        "message": "Get latest book successfully",
        "data": latest_book
    }


@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    book = next((b for b in books if b["id"] == book_id), None)

    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")

    return {
        "status": "success",
        "message": "Get book successfully",
        "data": book
    }