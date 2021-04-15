"""
Celeste Sila
April 15, 2021
Module 6.2
Assignment: Pytech: Updating Documents
Description: Updating documents in the Pytech database.
"""

# import statements 
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to MongoDB cluster 
client = MongoClient(url)

# connect to pytech database
db = client.pytech

# get students collection 
students = db.students

# find all students in collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over collection & output results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Kent  aka Kal-El"}})

# find updated student document 
kent = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output updated document
print("  Student ID: " + kent["student_id"] + "\n  First Name: " + kent["first_name"] + "\n  Last Name: " + kent["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")

