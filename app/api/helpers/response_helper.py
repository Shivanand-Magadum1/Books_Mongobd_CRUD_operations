def serialize_book(book):
    return {
        "id": str(book["_id"]),
        "name": book.get("name"),
        "writer": book.get("writer"),
        "genre": book.get("genre"),
    }
