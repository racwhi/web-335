
#Title: white_usersp2.py
#Author: Rachel White
#Date: 2/23/2025
#Description: Connects to a MongoDB database and performs CRUD operations on user documents.


# Import the MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']


# Step 3: Create a new user document
new_user = {
    "firstName": "Rachel",
    "lastName": "White",
    "employeeId": "1014",
    "email": "rachel.white@newuser.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
new_user_id = db.users.insert_one(new_user).inserted_id
print(f"New user created with id: {new_user_id}")

# Step 4: Prove the document was created
print("Document created:")
print(db.users.find_one({"employeeId": "1014"}))

# Step 5: Update the email address of the document
db.users.update_one(
    {"employeeId": "1014"},
    {
        "$set": {
            "email": "rw@me.com"
        }
    }
)

# Step 6: Prove the document was updated
print("Document after update:")
print(db.users.find_one({"employeeId": "1014"}))

# Step 7: Delete the document that was created
result = db.users.delete_one({"employeeId": "1014"})
print(f"Number of documents deleted: {result.deleted_count}")

# Step 8: Prove the document was deleted
print("Trying to find the deleted document:")
print(db.users.find_one({"employeeId": "1014"}))

