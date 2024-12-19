import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "BooksDatabase")

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

books_collection = db["Books"]
