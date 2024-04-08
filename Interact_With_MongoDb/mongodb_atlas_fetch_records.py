from pymongo import MongoClient

import mongodb_atlas_constants as constants

username, password = "admin", "password" # Replace with your own credentials

uri = f'{constants.MONGODB_ATLAS_URL.format(username=username, password=password)}' \
        f'{constants.MONGO_DB_NAME}'

# Create a new client and connect to the server
client = MongoClient(uri)
db = client[constants.MONGO_DB_NAME]
collection = db[constants.MONGO_COLLECTION_NAME]

try:
    # Fetch single record from the collection
    cursor = collection.find_one()
    # Print the document
    print(f"Record: {cursor}")
    print("\n==========\n")
    for i, j in cursor.items():
        print(f"{i}: {j}")

    # Fetch all records from the collection and convert it to a DataFrame
    cursor = collection.find()
    # Print the total no of documents
    print(f"Total Records: {len(list(cursor))}")
    print("\n==========\n")
    # Print the first 5 documents
    for i, doc in enumerate(cursor):
        if i < 5:
            print(f"Record {i+1}: {doc}")
            print("\n==========\n")
        else:
            break

except Exception as e:
    print(e)

# Close the connection
client.close()
