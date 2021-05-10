# JSON data import to mongoDB
# RUN ONCE
import os
import json
from flask import Flask
from flask_pymongo import PyMongo
if os.path.exists("env.py"):
    import env

# App setep
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)

# Upload json data to Mongo DB
# Data found to be incomplete so aggregated for more content rich data.


def load_json_data():
    # Load JSON Data and insert to MongoDB collection
    data = [json.loads(line) for line in open('data/recipes.json', 'r')]
    if isinstance(data, list):
        mongo.db.recipes.insert_many(data)
        mongo.db.recipes.aggregate([
            {"$match": {"photo_url": {"$exists": True, "$not": {"$type": 10}},
            "total_time_minutes": {"$gt": 0},
            "description": {"$exists": True},
            "$expr": {"$gt": [{"$strLenCP": "$description"}, 80]}
            }},
            {"$out": 'recipes_clean'}
        ])


load_json_data()
