import os
import random
import datetime
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
    recipes = list(mongo.db.recipes_clean.find())
    random.shuffle(recipes)
    return render_template("recipes.html", recipes=recipes)


# Search route
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes_clean.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


# Individual recipe route
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    # recipe id checked against database id
    recipe_id = mongo.db.recipes_clean.find_one({"_id": ObjectId(recipe_id)})
    if "user" in session:
        user_data = mongo.db.users.find_one({"username": session["user"]})
        user_recipes_ids = user_data.get('user_recipes')
        if session["user"] and user_recipes_ids:
            if recipe_id.get("_id") in user_recipes_ids:
                render = render_template(
                    "recipe.html", recipe_id=recipe_id,
                    user_recipe_id=recipe_id.get("_id"))
                return render
    else:
        return render_template("recipe.html", recipe_id=recipe_id)
    return render_template("recipe.html", recipe_id=recipe_id)


# Register user route
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if user exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # create timestamp for user activity
        time = datetime.datetime.now()
        timestamp = time.strftime("%d-%b-%Y (%H:%M:%S)")

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "fname": request.form.get("fname").lower(),
            "lname": request.form.get("lname").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "is_admin": "no",
            "created_on": timestamp,
            "last_active": timestamp,
            "last_ip": request.remote_addr,
            "submissions": 0,
            "active": True,
            "activity": ["User registered on: " + timestamp]
        }
        mongo.db.users.insert_one(register)
        # put new user into session
        session["user"] = request.form.get("username").lower()
        flash(f"Registration successful {session['user'].capitalize()}")
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


# Individual recipe route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if usern exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username".lower())})
        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                session["is_admin"] = existing_user["is_admin"]
                # update user data
                time = datetime.datetime.now()
                timestamp = time.strftime("%d-%b-%Y (%H:%M:%S)")
                mongo.db.users.update_one({
                    "_id": existing_user.get("_id")},
                    {"$set": {
                        "last_active": timestamp,
                        "last_ip": request.remote_addr,
                        "active": True
                    }
                })
                mongo.db.users.update_one({
                    "_id": existing_user.get("_id")},
                    {"$addToSet": {
                        "activity": "User logged in on: " + timestamp
                    }
                })
                name = request.form.get("username").capitalize()
                flash("Welcome, {}".format(name))
                render = redirect(
                        url_for("my_recipes", username=session["user"]))
                return render
            else:
                # incorrect password
                flash("Incorrect Username/ Password, please try again.")
                return redirect(url_for("login"))
        else:
            # username does not exist
            flash("Incorrect Username/ Password, please try again")
            return redirect(url_for("login"))

    return render_template("login.html")


# logout recipe route
@app.route("/logout")
def logout():
    # update user data
    existing_user = mongo.db.users.find_one(
            {"username": session["user"]}
    )
    # remove session vars
    session.pop("user")
    session.pop("is_admin", None)
    # create timestamp for user activity
    time = datetime.datetime.now()
    timestamp = time.strftime("%d-%b-%Y (%H:%M:%S)")
    mongo.db.users.update_one({
        "_id": existing_user.get("_id")},
        {"$set": {
            "last_active": timestamp,
            "last_ip": request.remote_addr,
            "active": False
        }
    })
    mongo.db.users.update_one({
        "_id": existing_user.get("_id")},
        {"$addToSet": {
            "activity": "User logged out on: " + timestamp
        }
    })
    # remove user session cookies
    flash("You have been successfully logged out")
    return redirect(url_for("login"))


# My Recipes profile page
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # session username checked against database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user_data = mongo.db.users.find_one({"username": username})
    user_recipes_ids = user_data.get('user_recipes')
    submited_recipes = list(
            mongo.db.recipes_clean.find({"chef_id": session["user"]}))
    # Pass username to my_recipes.html
    if session["user"]:
        # Check if user has pinned recipes for rendering in My Recipe profile
        if user_recipes_ids:
            user_recipes = []
            for object_id in user_recipes_ids:
                recipe = mongo.db.recipes_clean.find_one(
                        {"_id": ObjectId(object_id)})
                user_recipes.append(recipe)
                render = render_template(
                    "my_recipes.html", username=username,
                    user_recipes=user_recipes,
                    submited_recipes=submited_recipes)
            return render

    return render_template("my_recipes.html", username=username)


# Admin dashboard
@app.route("/admin")
@app.route("/admin/")
def admin():
    if session["is_admin"] == "yes":
        user_data = list(mongo.db.users.find())
        recipe_data = list(mongo.db.recipes_clean.find())
        chef_data = list(mongo.db.recipes_clean.aggregate([
                {"$group": {"_id": "$chef", "count": {"$sum": 1}}}, {"$sort": {"count": -1}}, {"$limit": 5},
                # {"$group": {"_id": "Chefs", "count": {"$sum": 1}}},
        ]))
        activity_data = list(mongo.db.users.aggregate([
                {"$group": {"_id": "$username", "total": { "$sum": { "$size":"$activity" } }}}
        ]))
    return render_template("admin.html", users=user_data, recipe_data=recipe_data, chef_data=chef_data,  activity_data=activity_data )


@app.route("/admin/user_activity/<user_id>")
def user_activity(user_id):
    user_activity = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return render_template("user_activity.html", user_data=user_activity)


# Pin recipe route
@app.route("/pin_recipe/<recipe_id>")
def pin_recipe(recipe_id):
    # Add recipe from recipes.html to user my recipes profile page
    recipe_id = mongo.db.recipes_clean.find_one({"_id": ObjectId(recipe_id)})
    # Check if recipe has already been added
    pinned_recipes = mongo.db.users.find({
            "username": session["user"],
            "user_recipes": {
                "$in": [ObjectId(recipe_id.get("_id"))], }}).count()
    if pinned_recipes == 1:
        flash("Error - Recipe already saved")
    else:
        mongo.db.users.update_one({
            "username": session[
                "user"]}, {
                    "$push": {
                        "user_recipes": recipe_id.get(
                            "_id")}}, upsert=True)
        flash("Recipe saved!")
    # Redirect to profile
    return redirect(url_for("my_recipes", username=session["user"]))


# Remove pinned recipe route
@app.route("/remove_recipe/<recipe_id>")
def remove_recipe(recipe_id):
    # Remove pinned recipe from user profile (recipe not deleted)
    user_id = mongo.db.users.find_one({"username": session["user"]})
    mongo.db.users.update({
        "_id": user_id.get("_id")}, {
            "$pull": {
                "user_recipes": ObjectId(recipe_id)}})
    flash("Recipe removed from Your Recipes")
    return redirect(url_for("my_recipes", username=session["user"]))


# Add recipe route
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    existing_user = mongo.db.users.find_one(
            {"username": session["user"]}
    )
    if request.method == "POST":
        recipe = {
            "chef": request.form.get("name"),
            "chef_id": session['user'],
            "cooking_time_minutes": int(request.form.get(
                "cooking_time_minutes")),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions"),
            "photo_url": request.form.get("photo_url"),
            "preparation_time_minutes": int(request.form.get(
                    "preparation_time_minutes")),
            "serves": request.form.get("serves"),
            "title": request.form.get("title"),
            "total_time_minutes": int(request.form.get(
                "cooking_time_minutes")) + int(request.form.get(
                    "preparation_time_minutes"))

        }
        mongo.db.recipes_clean.insert_one(recipe)
        if existing_user:
            mongo.db.users.update_one({
                "_id": existing_user.get("_id")},
                {"$inc": {
                    "submissions": 1
                }
            })
        flash("Your Recipe Has Been Successfully Added")
        return redirect(url_for("my_recipes", username=session["user"]))
    return render_template("add_recipe.html")


# Edit recipe route
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        edit = {
            "chef": request.form.get("name"),
            "chef_id": session['user'],
            "cooking_time_minutes": int(request.form.get(
                "cooking_time_minutes")),
            "description": request.form.get("description"),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions"),
            "photo_url": request.form.get("photo_url"),
            "preparation_time_minutes": int(request.form.get(
                "preparation_time_minutes")),
            "serves": request.form.get("serves"),
            "title": request.form.get("title"),
            "total_time_minutes": int(request.form.get(
                "cooking_time_minutes")) + int(request.form.get(
                    "preparation_time_minutes"))

        }
        mongo.db.recipes_clean.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Your Recipe Has Been Successfully Updated")

    recipe = mongo.db.recipes_clean.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


# Delete recipe route
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Delete user submitted receipe
    existing_user = mongo.db.users.find_one(
            {"username": session["user"]}
    )
    mongo.db.recipes_clean.remove({"_id": ObjectId(recipe_id)})
    if existing_user:
        mongo.db.users.update_one({
            "_id": existing_user.get("_id")},
            {"$inc": {
                "submissions": -1
            }
        })
    flash("Your submited Recipe has been deleted")
    return redirect(url_for("my_recipes", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get(
        "IP"), port=int(os.environ.get(
            "PORT")), debug=True)
# Debug True!!
