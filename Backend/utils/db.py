from pymongo import MongoClient, errors

def create_connection(host, port, username, password, db_name):
    client = None
    try:
        # Create a MongoDB client
        client = MongoClient(host=host, port=port, username=username, password=password, authSource=db_name)

        client.server_info() 
        print("MongoDB connection successful")
    except errors.ServerSelectionTimeoutError as err:
        # If connection is not successful, print the error
        print("PyMongo ERROR:", err)
        client = None
    except Exception as e:
        print("An error occurred:", e)
        client = None

    return client

def get_database(client, db_name):
    db = None
    try:
        db = client[db_name]
    except Exception as e:
        print(f"An error occurred while getting the database: {e}")

    return db

def get_collection(db, collection_name):
    collection = None
    try:
        collection = db[collection_name]
    except Exception as e:
        print(f"An error occurred while getting the collection: {e}")

    return collection