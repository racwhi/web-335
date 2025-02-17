"""
Title: users.py
Author: Rachel White
Date: 2/16/2025
Description: Python program to connect to MongoDB and perform various operations.
"""

# Import the MongoClient
from pymongo import MongoClient

# Build a connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@bellevueuniversity.mdmj7.mongodb.net/")


# Access the web335DB database
db = client['web335DB']

# --- Display all documents in the 'users' collection ---
for user in db.users.find():
    print(user)

# --- Display a document where the employeeId is 1011 ---
employee_1011 = db.users.find_one({"employeeId": "1011"})  #Corrected the data type to String
print(employee_1011)

# --- Display a document where the lastName is Mozart ---
mozart = db.users.find_one({"lastName": "Mozart"})
print(mozart)
