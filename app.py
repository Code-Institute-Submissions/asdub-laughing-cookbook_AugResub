import os
import random
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# App setep
app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Home
@app.route("/")
@app.route("/recipes")
def recipes():
    # filter data before being passed to UI
    recipes = list(mongo.db.recipes.find(
        {"photo_url": {"$exists": True, "$not": {"$type": 10}},
            "total_time_minutes": {"$gt": 0},
            "description": {"$exists": True},
            "$expr": {"$gt": [{"$strLenCP": "$description"}, 100]}
        }))
    random.shuffle(recipes)
    return render_template("recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # recipe id checked against database id
    recipe_id = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    if recipe_id:
        return render_template("recipe.html", recipe_id=recipe_id)

    return render_template("recipe.html", recipe_id=recipe)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": "no"
        }
        mongo.db.users.insert_one(register)
        # put new user into session
        session["user"] = request.form.get("username").lower()
        flash(f"Registration successful {session['user'].capitalize()}")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if usern exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username".lower())})
        if existing_user:
            # check hashed password matches user input
            if check_password_hash(existing_user["password"],
                request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["is_admin"] = existing_user["is_admin"]
                flash("Welcome, {}".format(request.form.get("username").capitalize()))
                return redirect(url_for("my_recipes", username=session["user"]))
            else:
                # incorrect password
                flash("Incorrect Username/ Password, please try again.")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username/ Password, please try again")
            return redirect(url_for("login"))
       
    return render_template("login.html")


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # session username checked against database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("my_recipes.html", username=username)

    return render_template("my_recipes.html", username=username)


@app.route("/logout")
def logout():
    #remove user session cookies
    flash("You have been successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)
# Debug True!!
