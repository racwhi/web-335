"""
Author : Rachel White
Date: 3/9/2025
Description: WhataBook application with Python and Mongo.
"""

try:
    import pymongo
    from pymongo import MongoClient
    from pymongo.errors import PyMongoError
    from datetime import datetime
except ImportError:
    exit("Pymongo is required to run this application. Install Pymongo using the command:\n"
         "pip install pymongo")


class Database:
    """
      MongoDB connections and queries.
    """

    def __init__(self, databaseURI=None, databaseName=None):
        """ INIT
            Initializes the Database class.
        """
        if not databaseURI or not isinstance(databaseURI, str):
            raise ValueError("Invalid database URI")
        if not databaseName or not isinstance(databaseName, str):
            raise ValueError("Invalid database name")

        self.databaseURI = databaseURI
        self.databaseName = databaseName
        self.connection = None
        self.database = None

    def connect(self):
        """ CONNECT
            Establishes a connection to the MongoDB database.
        """
        try:
            if self.connection is None:
                self.connection = MongoClient(self.databaseURI)
                self.database = self.connection[self.databaseName]
                print("MongoDB Connection was successful!")
        except Exception as e:
            exit(f"Connection error: {e}")

    def disconnect(self):
        """ DISCONNECT
            Closes the MongoDB connection if it is active.
        """
        if self.connection:
            self.connection.close()
            self.connection = None
            self.database = None

    def hasConnection(self) -> bool:
        """ Checks if there is an active connection to the database. """
        return self.database is not None and self.connection is not None

    def __enter__(self):
        """ Enter
            Establishes a connection to the MongoDB database when used in a `with` statement.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ EXIT
            Ensures the database connection is closed when exiting a `with` block.
        """
        self.disconnect()

    def findAll(self, collection: str, filter: dict = None, projection: dict = None) -> list:
        """ FIND ALL
            Retrieves all documents that match the filter.
        """
        if not collection or not isinstance(collection, str):
            raise ValueError("Collection name must be a non-empty string.")

        if filter is None:
            filter = {}

        if projection is None:
            projection = {"_id": 0}

        if self.database is None:
            self.connect()

        try:
            return list(self.database[collection].find(filter, projection))
        except PyMongoError as e:
            print(f"Database query failed: {e}")
            return []

    def addOne(self, collection: str, properties: dict) -> str:
        """ ADD ONE
            Inserts a new document .
        """
        if not collection or not isinstance(collection, str):
            raise ValueError("Collection name must be a non-empty string.")

        if not isinstance(properties, dict) or not properties:
            raise ValueError("Properties must be a non-empty dictionary.")

        if self.database is None:
            self.connect()

        try:
            result = self.database[collection].insert_one(properties)
            return str(result.inserted_id)
        except PyMongoError as e:
            print(f"Database insert failed: {e}")
            return ""


def init(dbUri: str, dbName: str):
    """ INIT
        handles initializing the WhatABook Console Application
    """
    if not dbUri or not isinstance(dbUri, str) or dbUri == '':
        exit("Invalid database URI!")

    if not dbName or not isinstance(dbName, str) or dbName == '':
        exit("Invalid database name!")

    def checkDbConnection():
        """ CHECK DB CONNECTION
            Connect to your MongoDB database.
        """
        print("Checking MongoDB database connection...\n")
        with Database(databaseURI=dbUri, databaseName=dbName) as db:
            if db.hasConnection():
                print("MongoDB Connection was successful!\n")
            else:
                print("MongoDB Connection failed!\n")

    def displayBookList():
        """ DISPLAY BOOK LIST
            Display a list of books.
        """
        print("List of Available Books:\n")

        with Database(databaseURI=dbUri, databaseName=dbName) as db:
            allBooks = db.findAll(collection='books')

            if allBooks:
                for index, book in enumerate(allBooks, start=1):
                    print(f"{index}. Title: {book['title']}, Author: {book['author']}")
            else:
                print("No books were found!\n")

    def addUser():
        """ ADD USER
            Adds a new user to the database.
        """
        print("Adding a New User:\n")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")  

        user_data = {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
            "password": password,  # Store hashes in production
            "dateCreated": datetime.utcnow().isoformat() + "Z"
        }
        
        with Database(databaseURI=dbUri, databaseName=dbName) as db:
            userId = db.addOne('customers', user_data)
            print(f"User added with ID: {userId}\n")

    def createWishlist():
        """ CREATE WISHLIST
            Create a wishlist for an existing user.
        """
        print("Creating a Wishlist:\n")
        customerId = input("Enter Customer ID: ")

        wishlist_data = {
            "customerId": customerId,
            "books": []
        }
        
        with Database(databaseURI=dbUri, databaseName=dbName) as db:
            wishlistId = db.addOne('wishlists', wishlist_data)
            print(f"Wishlist created with ID: {wishlistId}\n")
    
    def addBookToWishlist():
        """ ADD BOOK TO WISHLIST
            Adds a book to an existing user's wishlist.
        """
        print("Adding a Book to User's Wishlist:\n")
        wishlist_id = input("Enter Wishlist ID: ")
        book_id = input("Enter Book ID: ")

        with Database(databaseURI=dbUri, databaseName=dbName) as db:
            wishlist = db.findAll(collection='wishlists', filter={"wishlistId": wishlist_id})
            if wishlist:
                wishlist[0]['books'].append({"bookId": book_id})  # Append new book
                db.addOne('wishlists', wishlist[0])  
                print(f"Book {book_id} has been added to Wishlist {wishlist_id}.\n")
            else:
                print(f"Wishlist with ID {wishlist_id} not found!\n")

    def viewUserWishlist():
        """ VIEW USER WISHLIST
            Displays a user's wishlist.
        """
        print("Viewing User's Wishlist:\n")
        wishlist_id = input("Enter Wishlist ID: ")

        with Database(databaseURI=dbUri, databaseName=dbName) as db:
            wishlist = db.findAll(collection='wishlists', filter={"wishlistId": wishlist_id})
            if wishlist:
                print(f"Wishlist ID: {wishlist_id}\nBooks: {wishlist[0]['books']}\n")
            else:
                print(f"Wishlist with ID {wishlist_id} not found!\n")

    # Execute defined functions
    checkDbConnection()
    displayBookList()
    addUser()
    createWishlist()
    addBookToWishlist()
    viewUserWishlist()


# Initialize the application
app = init(
    dbUri="mongodb+srv://web335_user:s3cret@bellevueuniversity.mdmj7.mongodb.net/",
    dbName="WhatABook"
)
