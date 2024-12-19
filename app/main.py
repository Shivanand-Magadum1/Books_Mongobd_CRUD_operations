from fastapi import FastAPI
from app.api.controllers.books_controller import books_router

app = FastAPI(
    title="FastAPI with MongoDB - Books API",
    description="CRUD operations for books using FastAPI and MongoDB",
    version="1.0.0",
)

# Include the books router
app.include_router(books_router, prefix="/books", tags=["Books"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI MongoDB Books API"}

