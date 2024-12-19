from pydantic import BaseModel, Field
from typing import Optional


class BookModel(BaseModel):
    name: str = Field(...)
    writer: str = Field(...)
    genre: str = Field(...)


class UpdateBookModel(BaseModel):
    name: Optional[str] = None
    writer: Optional[str] = None
    genre: Optional[str] = None

