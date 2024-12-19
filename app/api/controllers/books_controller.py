from fastapi import APIRouter, HTTPException, Query
from app.api.services.book_services import (
    create_new_book,
    get_all_books,
    get_book_by_id,
    update_existing_book,
    delete_book_by_id,
)
from app.api.models.book_models import BookModel, UpdateBookModel

books_router = APIRouter()

# Create a new book
@books_router.post("/", response_description="Add a new book")
def create_book(book: BookModel):
    return create_new_book(book)


# Get all books with pagination
@books_router.get("/", response_description="List all books with pagination")
def get_books(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
):
    return get_all_books(page, size)


# Get a single book by ID
@books_router.get("/{book_id}", response_description="Get a single book by ID")
def get_book(book_id: str):
    return get_book_by_id(book_id)


# Update a book by ID
@books_router.put("/{book_id}", response_description="Update a book by ID")
def update_book(book_id: str, updated_book: UpdateBookModel):
    return update_existing_book(book_id, updated_book)


# Delete a book by ID
@books_router.delete("/{book_id}", response_description="Delete a book by ID")
def delete_book(book_id: str):
    return delete_book_by_id(book_id)

