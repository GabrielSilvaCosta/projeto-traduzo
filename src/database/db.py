# src/database/db.py
import os
from pymongo import MongoClient

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
DB_NAME = os.environ.get('DB_NAME', 'test_db_traduzo')

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
