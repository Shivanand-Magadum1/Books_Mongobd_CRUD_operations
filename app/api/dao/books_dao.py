from app.api.utility.db import books_collection


def insert_book(book_data):
    return books_collection.insert_one(book_data).inserted_id


def find_books(skip: int, size: int):
    books_cursor = books_collection.find().skip(skip).limit(size)
    total_books = books_collection.count_documents({})
    return books_cursor, total_books


def find_book_by_id(book_id):
    return books_collection.find_one({"_id": book_id})


def update_book(book_id, updated_data):
    return books_collection.update_one({"_id": book_id}, {"$set": updated_data}).modified_count


def remove_book_by_id(book_id):
    return books_collection.delete_one({"_id": book_id}).deleted_count



