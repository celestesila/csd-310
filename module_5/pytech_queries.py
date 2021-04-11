"""
Celeste Sila
April 10, 2021
Assignment: pytech_queries.py
Description: Test program for querying the students collection.
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

# find students in collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# output results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# find document by student_id
bruce = students.find_one({"student_id": "1008"})

# output the results 
print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + bruce["student_id"] + "\n  First Name: " + bruce["first_name"] + "\n  Last Name: " + bruce["last_name"] + "\n")


# exit message 
input("\n\n  End of program, press any key to continue...")

