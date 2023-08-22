import pandas as pd
from pymongo import MongoClient

# Load data from the JSON file
input_file_path = "/opt/data/data.json"
with open(input_file_path, "r") as file:
    data = file.read()

# Parse JSON data
parsed_data = pd.read_json(data)
extracted_text = parsed_data["text"]

# Connect to the MongoDB instance
client = MongoClient("mongodb://mongodb-container")
# client = MongoClient("mongodb://localhost:27017/")
db = client["Datacat"]
collection = db["Collcat"]

# Insert data into MongoDB
# records = extracted_text.to_dict(orient="records")
# collection.insert_many(records)
for text in extracted_text:
    document = {"text": text}
    collection.insert_one(document)

print("Data imported into MongoDB", "\n", extracted_text)


# print("Text: ", extracted_text)
