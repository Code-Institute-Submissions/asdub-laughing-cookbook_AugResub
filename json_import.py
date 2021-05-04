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


def load_json_data():
    # Load JSON Data and insert to MongoDB collection
    data = [json.loads(line) for line in open('data/recipes.json', 'r')]
    if isinstance(data, list):
        mongo.db.recipes.insert_many(data)


load_json_data()
