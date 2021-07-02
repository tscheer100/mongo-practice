import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv("./.env")
# PWD = os.getenv('PWD')
MONGO_CLIENT_URL = os.getenv('MONGO_CLIENT_URL')

# cluster = MongoClient(f"mongodb+srv://Turtle:{PWD}@cluster0.m60hy.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
cluster = MongoClient(MONGO_CLIENT_URL)
db = cluster["database"]
collection = db["test"]

post = {'_id': 0, 'name': 'Thomas', 'score': 5}

collection.insert_one(post)