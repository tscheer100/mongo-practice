import os
import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv


load_dotenv("./.env")
MONGO_CLIENT_URL = os.getenv('MONGO_CLIENT_URL')

cluster = MongoClient(MONGO_CLIENT_URL)
db = cluster["database"]
collection = db["test"]

# add one collection to DB
# ------------------------------
# post = {'_id':0, 'name:':'Thomas', 'score':5}
# collection.insert_one(post)

# add multiple collections to db
# ------------------------------ 
# post1 = {'_id': 5, "name":"joe"}
# post2 = {'_id': 6, 'name':'bill'}
# collection.insert_many([post1, post2])

# how to find a result 
# ------------------------------ 
# results1 = collection.find({'name':'bill'}) # regex also works with this
# # |btw, it's also possible to find a collection using multiple variables|
# # |results = collection.find({'_id':2,'name':'james'})                  |
# ########## print(results) <=== this will not work. it will return an object of gibberish. BAD
# # do this instead
# for result in results1:
#     print(result['_id'])

# # but this returns a cursor object because we had to loop through all of the results. 
# # if we want to go through a single result, we do this
# results2 = collection.find_one({'_id':0})
# print(results2)

# # quickly, there is a way to delete collections
# results = collection.delete_one({'_id':0})
# # or to deleete many 
# reults = collection.delete_many({'name':'Bill'})

# # we can also replace data in a collection. to do this, we are going to need to reference the update operators docs: 
# # https://docs.mongodb.com/manual/reference/operator/update/
# results = collection.update_one({'_id':5}, {'$set':{'name':'Jimmy'}})
# # to add a new field, just add it like so
# results = collection.update_one({'_id':5}, {'$set':{'score':10}})
# # let's see what happens when we use the increment command instead of. 
# results = collection.update_one({'_id':5}, {'$inc':{'score':10}})
# as you can see, the score is now 20 beacuse it increments it by 10.

# # there is a way we can count the number of a document in a db. let's say we wanted to count all of the documents.
# # we would do this
post_count = collection.count_documents({})
print(post_count)
# # or if we wanted to count the amount of documents with a specific type, we would do something like this
jimmy_count = collection.count_documents({'name':'Jimmy'})
print(jimmy_count)