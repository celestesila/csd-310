"""
Celeste Sila
April 10, 2021
Assignment: pytech_insert.py
Description: Test program for inserting new documents into students collection 
"""

# import statements
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.rsnru.mongodb.net/pytech?retryWrites=true&w=majority"

# connect to MongoDB cluster 
client = MongoClient(url)

# connect pytech database
db = client.pytech

# document for Clark Kent 
clark = {
    "student_id": "1007",
    "first_name": "Clark",
    "last_name": "Kent",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "4.0",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "WRM101",
                    "description": "Introduction to W.O.R.M.S.",
                    "instructor": "Professor Bravo",
                    "grade": "A+"
                },
                {
                    "course_id": "BBL101",
                    "description": "Introduction to Operation Sunspot",
                    "instructor": "Professor Bubbles",
                    "grade": "A+"
                }
            ]
        }
    ]

}

# document for Bruce Wayne 
bruce = {
    "student_id": "1008",
    "first_name": "Bruce",
    "last_name": "Wayne",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.52",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "WRM101",
                    "description": "Introduction to W.O.R.M.S.",
                    "instructor": "Professor Bravo",
                    "grade": "B+"
                },
                {
                    "course_id": "BBL101",
                    "description": "Introduction to Operation Sunspot",
                    "instructor": "Professor Bubbles",
                    "grade": "A-"
                }
            ]
        }
    ]
}

# document for Arthor Curry
arthur = {
    "student_id": "1009",
    "first_name": "Arthur",
    "last_name": "Curry",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "1.5",
            "start_date": "July 10, 2020",
            "end_date": "September 14, 2020",
            "courses": [
                {
                    "course_id": "WRM101",
                    "description": "Introduction to W.O.R.M.S.",
                    "instructor": "Professor Bravo",
                    "grade": "C"
                },
                {
                    "course_id": "BBL101",
                    "description": "Introduction to Operation Sunspot",
                    "instructor": "Professor Bubbles",
                    "grade": "B"
                }
            ]
        }
    ]
}

# get students collection 
students = db.students

# insert statement and output 
print("\n  -- INSERT STATEMENTS --")
clark_student_id = students.insert_one(clark).inserted_id
print("  Inserted student record Clark Kent into the students collection with document_id " + str(clark_student_id))

bruce_student_id = students.insert_one(bruce).inserted_id
print("  Inserted student record Bruce Wayne into the students collection with document_id " + str(bruce_student_id))

arthur_student_id = students.insert_one(arthur).inserted_id
print("  Inserted student record Arthur Curry into the students collection with document_id " + str(arthur_student_id))

input("\n\n  End of program, press any key to exit... ")
