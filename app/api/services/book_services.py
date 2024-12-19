from fastapi import HTTPException
from bson import ObjectId
from app.api.dao.books_dao import (
    insert_book,
    find_books,
    find_book_by_id,
    update_book,
    remove_book_by_id,
)
from app.api.helpers.response_helper import serialize_book
from app.api.models.book_models import BookModel, UpdateBookModel


def create_new_book(book: BookModel):
    new_book_id = insert_book(book.dict())
    created_book = find_book_by_id(new_book_id)
    return serialize_book(created_book)


def get_all_books(page: int, size: int):
    skip = (page - 1) * size
    books_cursor, total_books = find_books(skip, size)
    books = [serialize_book(book) for book in books_cursor]
    total_pages = (total_books + size - 1) // size
    return {"total": total_books, "page": page, "size": size, "total_pages": total_pages, "books": books}


def get_book_by_id(book_id: str):
    book = find_book_by_id(ObjectId(book_id))
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return serialize_book(book)


def update_existing_book(book_id: str, updated_book: UpdateBookModel):
    update_result = update_book(ObjectId(book_id), updated_book.dict(exclude_unset=True))
    if not update_result:
        raise HTTPException(status_code=404, detail="Book not found or no changes made")
    return serialize_book(find_book_by_id(ObjectId(book_id)))


def delete_book_by_id(book_id: str):
    if not remove_book_by_id(ObjectId(book_id)):
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted successfully"}

