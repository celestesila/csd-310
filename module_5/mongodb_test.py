"""
Celeste Sila
April 10, 2021
Assignment: mongodb_test.py
Description: Test program for inserting new documents into students collection 
"""

# import statement
from pymongo import MongoClient

# connection string 
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# show connected collections 
print("\n -- Pytech COllection List --")
print(db.list_collection_names())

# show exit message
input("\n\n  End of program, press any key to exit... ")
