"""
Celeste Sila
April 15, 2021
Module 6.3
Assignment: Pytech: Deleting Documents
Description: Deleting documents in the Pytech database.
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

# loop over collection and output results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# add document 
add_doc = {
    "student_id": "1010",
    "first_name": "Alan",
    "last_name": "Scott"
}

# insert document into MongoDB atlas 
add_doc_id = students.insert_one(add_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(add_doc_id))

# call find_one() method by student_id 1010
student_add_doc = students.find_one({"student_id": "1010"})

# display results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_add_doc["student_id"] + "\n  First Name: " + student_add_doc["first_name"] + "\n  Last Name: " + student_add_doc["last_name"] + "\n")

# call delete_one method to remove newly added doc
deleted_student_add_doc = students.delete_one({"student_id": "1010"})

# find all students in collection 
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")