# The Cookbook

![GitHub contributors](https://img.shields.io/github/contributors-anon/asdub/laughing-cookbook)
![GitHub top language](https://img.shields.io/github/languages/top/asdub/laughing-cookbook)
![GitHub language count](https://img.shields.io/website?up_message=Online&url=http%3A%2F%2Flaughing-cookbook.herokuapp.com%2F)
![GitHub last commit](https://img.shields.io/github/last-commit/asdub/laughing-cookbook)

**A live version of this project can be found [here](http://laughing-cookbook.herokuapp.com/)**

<img src="https://github.com/asdub/laughing-cookbook/blob/master/readme/screenshots/iphone_screenshot.png" width="150" alt="The Cookbook on Mobile" />


### Project Description
This project was made as part of the Code Institute Full Stack Development Course. 

I have created a cooking recipe app.\
Allowing users to discover new recipes and submit their own for other users to enjoy. 

Users can pin discovered recipes and manage their own submitted ones. 
An administration dashboard gives an overview of users, advertising and statistics.  

<img src="https://github.com/asdub/laughing-cookbook/blob/master/readme/screenshots/macbook_screenshot.png" alt="The Cookbook on Desktop"/>


## Contents 

* [User Experience (UX)](#user-experience-ux)
    * [Brief](#Brief)
    * [Project Aims](#the-aim-of-this-project-is-to)
    * [User Stories](#new-user-stories)
* [Design](#design)
    * [Frameworks (front-end)](#frameworks-front-end)
    * [Colours](#colours)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Iconography](#iconography)
    * [Responsive](#responsive)
    * [App Flow](#appflow)
    * [Database Design](#databasedesign)
    * [Features](#features)
    * [Future Features](#future-features)
* [Technologies](#technologies)
    * [Languages](#languages)
    * [MongoDB & Dataset](#mongodb--dataset)
    * [Frameworks (back-end)](#frameworks-back-end)
    * [Dependencies](#dependencies)
    * [Version Control & Managment](#version-control--managment)
    * [Software/ Tools Used](#other-software-tools-used)
* [Deployment](#deployment)
    * [Fork](#fork)
    * [Clone (Locally)](#clone-locally)
    * [Heroku](#deploy-on-heroku)
* [Testing](#testing)
    * [W3C HTML](#wc3-html-validator-results)
    * [JS Hint](#js-hint)
    * [PEP8](#pep8)
    * [W3C CSS](#wc3-css-validator-results)
    * [Google Lighthouse](#google-lighthouse)
        * [Initial Test](#initial-test)
        * [Re-Test](#re-test)
    * [Manual Testing](#manual-testing)
        * [Testing Documentaition](https://github.com/asdub/laughing-cookbook/blob/master/readme/test/TESTME.md)
        * [User Stories Testing](#user-stories-testing)
    * [Known Bugs](#known-bugs)
    * [Credits](#credits)




## User Experience (UX)


### Brief

My intention was to create a simple app that presents its purpose immediately. 
Users can easily discover & manage recipes. And can also submit and manage their own personal recipes. 
Having previously designed my own layouts and styles, I wanted to use a front-end framework for this project. 
The app has been built using the [Materialize](https://materializecss.com/) front-end framework.


App users will likely be keen on food and cooking. 
However, given the variety of recipes available there should be something for all age groups and demographics. 


#### The aim of this project is to:
- Be simple and easy to use (as always!)
- Visually pleasing. 
- Provide users with a structured and easy to navigate catalog of recipes. 
- Allow users to pin recipes to their one 'My Recipes' profile. 
- Allow users to submit and manage their own recipes (CRUD). 
- Provide defensive design in terms of data editing or deletion. 
- Provide seamless login/ registration functionality.
- Allow administrators to manage any recipe. 
- Provide an admin dashboard giving a site overview. 
- Provide administrator functionality to manage advertising partners. 
- Provide a clear help section.


#### Business/ Monetisation
- The app provides functionality for advertising partners. Managed by the administrator.
- Provide an administrator with an app overview in the form of a dashboard.


#### New User Stories
- I want the app purpose to be obvious or easy to figure out
- I want to have access to the information available in as few steps of possible
- I want to be able to quickly search for a recipe. 
- I would like to store recipes of interest to me. 
- I would like to store and share my own recipes.


#### Returning & Regular User Stores
- I would like to manage my saved recipes. 
- I would like the ability to edit my own recipes. 
- I would like the ability to also delete my own recipes. 


## Design 

### Frameworks (front-end)
The [Materialize](https://materializecss.com/) front-end framework was used to style this app. 
With some additional custom css. 

The app uses the following components:
- [Badges](https://materializecss.com/badges.html)
- [Buttons](https://materializecss.com/buttons.html)
- [Cards](https://materializecss.com/cards.html)
- [Collections](https://materializecss.com/collections.html)
- [Footer](https://materializecss.com/footer.html)
- [Navbar](https://materializecss.com/navbar.html)
- [Modals](https://materializecss.com/modals.html)
- [Sidenav](https://materializecss.com/sidenav.html)
- [Tooltips](https://materializecss.com/tooltips.html)
- [Text Inputs](https://materializecss.com/text-inputs.html)


### Colours 
A limited palette of colours was used throughout the app.
As the app contains dynamically loaded imagery I thought it best to limit the use of colours to avoid potential colour clashing. 

**There are six colours used in total throughout the app.**

Orange - *#fb8c00*\
![Orange](https://github.com/asdub/laughing-cookbook/blob/master/readme/colours/fb8c00.png "Orange - #fb8c00")

Teal - *#00bfa5*\
![Teal](https://github.com/asdub/laughing-cookbook/blob/master/readme/colours/00bfa5.png "Teal - #00bfa5")

Grey - *#fafafa*\
![Grey](https://github.com/asdub/laughing-cookbook/blob/master/readme/colours/fafafa.png "Grey - #fafafa")

**These are used for text and delete buttons**: 

Red - *#f44335*\
![Red](https://github.com/asdub/laughing-cookbook/blob/master/readme/colours/f44335.png "Red - #f44335")

Black - *#212121*\
![Black](https://github.com/asdub/laughing-cookbook/blob/master/readme/colours/212121.png "Black - #212121")

White - *#ffffff*\
![Whtie](https://github.com/asdub/laughing-cookbook/blob/master/readme/colours/ffffff.png "White - #ffffff")


### Wireframes 

![Wireframes](https://github.com/asdub/laughing-cookbook/blob/master/readme/wireframes.png "Wireframes")

Mock Ups were completed for desktop, tablet & mobile devices. 

Wireframes can be viewed in full resolution [here on Adobe XD](https://xd.adobe.com/view/07051529-26a9-46df-84cf-76d5c9ea2a4e-5256/ "Wireframes").


### Typography

[Materialize](https://materializecss.com/) uses [Google Fonts](https://fonts.google.com/).

Only one font is in use:\
**Roboto** in weights of 400, 500 & 600.

<img src="https://github.com/asdub/laughing-cookbook/blob/master/readme/screenshots/roboto_font.png" width="150" alt="Google Fonts - Roboto" />


### Iconography

All icons in this project are from [Font Awesome](https://fontawesome.com/).

The following icons have been used throughout the app:\
<img src="https://github.com/asdub/laughing-cookbook/blob/master/readme/screenshots/icons.png" width="250" alt="Font Awesome Icons Used"/>


### Responsive 

The app uses the [Materialize](https://materializecss.com/) front-end framework.
Which is fully responsive. Materialize uses a 12 column grid system for layout.

The app renders in three layouts for mobile, tablet and desktop. 


### App Flow
*App Flow Diagram*
<img src="https://github.com/asdub/laughing-cookbook/blob/master/readme/appflow.png" alt="App Flow Diagram"/>


Users will initially land at */recipes*, styled as *'Discover Recipes'*. Available to all user types. 
Unregistered users can navigate to the individual recipe views by clicking *'View Recipe'*. 
At all times they can navigate back to *'Discover Recipes'*, *'Login'*, or *'Register'* via the navigation bar (or sidebar on mobile). 

Logged in users have the ability to access their *'My Recipes'* view and have access to the *'Add Recipe'* functionality. Users have additional options available to them such as edit and delete functions - these are explored in further detail in the [Features](#features) section below. 

The navigation/side bar displays different options once logged in, *'Login'* & *'Register'* are replaced with *'My Recipes'*, *'Add Recipe'* and *'Logout'*. 

A user logged in with admin privileges has an additional navigation option - *'Admin Dashboard'*. From there an administrator has access to an overview of the app. And has further functions available to them in terms of site advertising.


### Database Design

The app uses a document-oriented database, MongoDB. A NoSQL database program.
This solution was chosen as it provides the best flexibility for adding future features such as expanding the datasource to include further relevant data. And was the solution I was most confident in deploying. 

*Database Overview Diagram*
<img src="https://github.com/asdub/laughing-cookbook/blob/master/readme/database_overview.png" alt="Database Diagram"/>


The database contains 5 collections. 
- advert_data
- recipes
- recipes_clean
- site_data
- users

**More in depth informaton on this subject can be found below within the [Data](##mongodb--dataset) section below**

I orginally wanted to use an API to provide recipe content for the app. However, this provided impossible to locate without a paid subcription or poor qaulity content, so I opted to used a suitable dataset of recipes instead.


##### Document Structure: **advert_data**:
```
{
  "_id": {
    "$oid": "6098ff0addfddbb58a9c2f03"
  },
  "advertiser": "Le Creuset",
  "advertiser_id": "le_creuset",
  "category": "cookware",
  "partner_url": "https://www.lecreuset.ie/en_IE/",
  "partner_text": "For the best in cookware",
  "discount_rate": {
    "$numberInt": "10"
  },
  "discount_code": "thecookbook"
}

```
This collection provides a data source for the apps advertising. Check out the [current](#features) and potential [future features](#features) here.


##### Document Structure: **recipe / recipe_clean**:
```
{
  "_id": {
    "$oid": "6091b6e6215627810515bbce"
  },
  "chef": "Mary Berry",
  "chef_id": "mary_berry",
  "cooking_time_minutes": {
    "$numberInt": "0"
  },
  "description": "This is my standby pasta supper as it is so delicious, so quick and everyone loves it. Great for everyday or for casual supper parties too.",
  "error": false,
  "ingredients": [
    "350g/12oz penne pasta",
    "2 x 80g/3oz packs Parma ham, snipped into small pieces",
    "250g/9oz small brown chestnut mushrooms, halved or quartered",
    "200g/7oz full-fat crème fraîche",
    "100g/3½oz Parmesan, grated",
    "2 tbsp chopped parsley",
    "salt and pepper, to taste",
    "green salad",
    "crunchy bread"
  ],
  "instructions": [
    "Cook the pasta in a pan of boiling salted water according to the packet instructions. Drain and set aside",
    "Heat a frying pan until hot. Add the pieces of Parma ham and fry until crisp, remove half of the ham onto a plate and set aside. Add the mushrooms to the pan and fry for two minutes. Add the crème fraîche and bring up to the boil. Add the pasta, Parmesan and parsley and toss together over the heat. Season well with salt and pepper.",
    "Serve with a green salad and crunchy bread."
  ],
  "instructions_detailed": [
    {
      "ingredient": "pasta",
      "line": "350g/12oz penne pasta"
    },
    {
      "ingredient": "ham",
      "line": "2 x 80g/3oz packs Parma ham, snipped into small pieces"
    },
    {
      "ingredient": "chestnut mushrooms",
      "line": "250g/9oz small brown chestnut mushrooms, halved or quartered"
    },
    {
      "ingredient": "crème fraîche",
      "line": "200g/7oz full-fat crème fraîche"
    },
    {
      "ingredient": "Parmesan",
      "line": "100g/3½oz Parmesan, grated"
    },
    {
      "ingredient": "parsley",
      "line": "2 tbsp chopped parsley"
    },
    {
      "ingredient": "pepper",
      "line": "salt and pepper, to taste"
    },
    {
      "ingredient": "salad",
      "line": "green salad"
    },
    {
      "ingredient": "bread",
      "line": "crunchy bread"
    }
  ],
  "photo_url": "https://ichef.bbci.co.uk/food/ic/food_16x9_608/recipes/15_minute_pasta_33407_16x9.jpg",
  "preparation_time_minutes": {
    "$numberInt": "30"
  },
  "program": "Mary Berry Cooks",
  "program_id": "p01s4q10",
  "serves": {
    "$numberInt": "6"
  },
  "time_scraped": {
    "$numberInt": "1499227763"
  },
  "title": "15 minute pasta",
  "total_time_minutes": {
    "$numberInt": "30"
  },
  "url": "http://bbc.co.uk/food/recipes/15_minute_pasta_33407"
}
```
The recipe collection document stucture followed through from its JSON key pairs from the dataset.
It is a rather extensive collection of recipes (10,601!) from BBC cookery programs. 
For the purposes of this app I created a futher collection, recipe_clean containing 1900+ recipes (some of which are user submitted). This was to ensure that the data always had the required field values to A) avoid errors and B) ensure content quality. 

I maintained the fields that are presently unused for potential future features, which I explore in the [Future Features](#future-features) section. 


##### Document Structure: **recipe / site_data**:
```
{
  "_id": {
    "$oid": "60990015ddfddbb58a9c2f06"
  },
  "active_advertiser": "cuisinart"
}
```
This is a relatively sparse collection at present, it currently only stores the active advertiser. 
My view is that this collection would be used for any future site specific variables, perhaps themes or the site content itself. 


##### Document Structure: **recipe / user_data**:
```
{
  "_id": {
    "$oid": "6098108592a14a6700096d7c"
  },
  "fname": "pat",
  "lname": "mustard",
  "username": "pmustard",
  "password": "pbkdf2:sha256:150000$4Q2YQLD2$480c809281d82d801c2783a00bba21f86aa3be51d69bb1faef9429828d6ca07e",
  "is_admin": "no",
  "created_on": "09-May-2021 (16:40:37)",
  "last_active": "09-May-2021 (16:40:57)",
  "last_ip": "10.12.1.183",
  "submissions": {
    "$numberInt": "0"
  },
  "active": false,
  "activity": [
    "User registered on: 09-May-2021 (16:40:37)",
    "User logged out on: 09-May-2021 (16:40:57)"
  ],
  "user_recipes": [
    {
      "$oid": "6091b6e6215627810515c6e9"
    }
  ]
}
```


### Features

The Cookbook is a database driven app providing the following functionality:

**Navigation**
- The app has a dynamic menu structure. Providing a standard horizontal navbar on medium and large screens, and a hamburger menu with sidebar when used via a small/ mobile screen.  
- An unregistered user has the navigation options of: *'Discover Recipes'*, *'Log In'* and *'Register'*. 
- An authorised user has the following options: *'Discover Recipes'*, *'Your Recipes'*, *'Add Recipe'* and *'Log Out'*
- In addition to the above, an admin user also has access to *'Admin Dashboard'*

**Register** - *(/register)*
- Provides the user with a registration form. 
- A CTA is in place under the login form inviting a user to login if already registered. 
- Once submitted, a user is redirected to their 'My Recipes' profile. 
- A notification will appear in the top right corner of the screen welcoming the user. 

**Login** - *(/login)*
- Provide the user with a login form. 
- Once authenticated, a user is redirected to their 'My Recipes' profile. 
- A CTA is in place under the login form inviting a user to register. 
- A notification will appear in the top right corner of the screen welcoming the user. 

**Log Out** - *(/logout)*
- Provides logout functionality. 
- A user is redirected to the login form. 
- A notification will appear in the top right corner confirming log out. 

**Discover Recipes** - *(/recipes)*
- A count of current recipes is provided within the welcome text. 
- Search functionality is provided, a user can search title text, recipe description, and chef name. 
- On load the user will be presented with 20 recipe cards, which are randomised on each page reload. 
  - Each recipe card contains an image, title, description, a pin recipe button (if logged in), the recipes time and a link to *'View Recipe'* to proceed to the recipe page. 
- The user can pin a recipe to their 'My Recipe' profile or click 'View Recipe to see more information (once authorised). 
- An administrator has the ability to edit any recipe from this view. 

**Recipe** - *(/recipe/<recipe_id>)*
- This view gives the user the complete recipe including ingredients and instructions. 
- Under the description, an unauthorised user will see a login button. 
  - If authorised, this button will change to a pin or unpin recipe button.
  - If the user submitted the recipe in view they will have the option to delete and edit. 
  - An administrator can delete and edit any recipe. 
  - Defensive design is present here, when deleting a recipe a modal will appear to confirm the users choice. 
  - In addition to the recipe related content, advertising content is displayed under the recipes timings. 
    - This content is stored in the advert_data database collection mentioned above. 
    - An administrator can change the active advertiser from the admin dashboard. 

**Add Recipe** - *(/add_recipe)*
- This view provides the user with the ability to add a recipe to the database.
- The form, which provides validation and feedback to the user, has the following fields: 
  - Display Name - Pre-populated, the user can choose a display name 
  - Recipe Name 
  - Prep Time/ Cook Time/ Servings
  - Recipe Description 
  - Ingredients - additional lines can dynamically be added. 
  - Instructions - additional lines can dynamically be added. 
  - Photo URL 
- Once submitted, the user is redirected to their 'My Recipes Profile'
- A notification will appear in the top right corner confirming the recipe has been added. 

**Edit Recipe** - *(/edit_recipe/<recipe_id>)*
- A user can edit their previously submitted recipe. 
- The fields are pre-populated with the stored values which the user can freely edit and save. 
- An administrator has this functionality available for any recipe. 
- A notification will appear in the top right corner confirming the recipe has been updated. 

**Delete Recipe** - *(/delete_recipe/<recipe_id>)*
- Provides the functionality to delete a recipe. 
- This functionality is only available if the user submitted the recipe selected. 
- An administrator can delete any recipe. 
- A notification will appear in the top right corner confirming deletion of the recipe. 

**Pin /Unpin Recipes**
- A user can pin any recipe in the database. 
- A user can unpin any previously pinned recipe. 
- This functionality is available on the recipe card and also within the individual recipe view. 

**Your Recipes** - *(/my_recipes/<user_id>)*
- Provides this user with their own recipe collection. 
- The view is divided into two groups:
  - Submitted Recipes 
  - Pinned Recipes
- From this view a user can view, edit or delete their recipe card. 
  - When selecting delete, a notification appears above the button reaffirming the users action. Once clicked/ tapped a confirmation modal overlay will appear informing the user of the recipe title they are deleting. Their action is required to confirm the deletion. 
- In the pinned recipes section, a user can choose to view and unpin a pinned recipe card, 

**Recipe**  - *(/recipe/<recipe_id>)*
- This view displays the complete recipe. 
- The recipe information provided to the user are: 
 - Recipe Name
 - Recipe Chef/ Author
 - Recipe Image
 - Recipe Description
 - Recipe Timing & Servings Count
 - Recipe ingredients 
 - Recipe Instructions
- Below the recipe description, a user can pin the recipe being viewed. If already pinned, they can unpin the recipe. Or if it is one of their own submitted recipes they have the options to edit or delete the recipe. 
- An administrator has the edit and delete options for any recipe. 
- This view has a section for advertising, controlled via the admin dashboard.


**Admin Dashboard**  - *(/admin)*
- This view is only available to admin users only. 
- It provides three areas of overview - Users, Advertising & Statistics.

*Users*

- The user section displays a card for each user displaying: 
  - User activity - the user fontawesome icon is solid for active users. 
  - Username 
  - Users full name 
  - User last active time and date
  - Users last activity (limited to login/logout/registration events at present)
  - A recipe submission counter 
  - A link to view user activity view
    - Which displays all the users activity in a table within a seperate view. 
    - This view contains a 'Back to Admin Dashboard' and the end of the activity records.

*Advertising*

- This section displays the current advertiser active on the app. 
- An admin can change the active advertiser via the list displayed. 
- Selecting a different advertiser evokes the advertising function which updates the database with the new active advertiser, in turn changing the data being displayed on the 'Recipe' view advert, and then redirects the admin back to where they were. 

*Statistics*

- This section gives the admin a count of recipes in the database. 
- The number of registered users. 
- Two bar charts:
  - Displaying the top 5 chefs by recipe count.
  - The most active users by activity count. 


### Future Features 

#### Recipes Collection
I would like to expand on the data being presented to the user. 
While outside the scope of this project (and my present ability!), I would like to include the TV program information contained within the collection. This could be potentially used to find the episode in question and present a video of the recipe being made by the chef to the user or a link to the platform it is available on. 

The detailed ingredients data could be used in conjunction with a supermarkets api (not in Ireland!) to show the user the total cost of the recipe, and the ability to order the goods required to make it. 
Avenues such as this provide further monetisation routes for the app. 

#### Users Collection
I would like to expand on storing user activity to include recipe submission, edit & deletion events. 

A user profile which other users can interact with, perhaps ask questions about recipes submitted and leave feedback for the chef. The int variable count of users submission could be explained on here to create a user scoring system, giving awards in the form of profile icons when certain milestones are reached in terms of submissions or feedback received. 

The ability for registered users to leave text reviews and ratings for each recipe. The recipes score could be displayed on the recipe card. 

#### Site Data Collection
All site content (excluding recipes) would be stored in this collection. 
I would like the admin to have the functionality to edit any content on the app from the app itself. 

#### Advert Data Collection
A selection of partners could be added to this collection. The ability for the administrator to add to this collection from the app. And perhaps have adverts apply based on specific recipe keywords, or the date and time. 

#### Filtering
I would like to provide the user with a dropdown of filters applicable to the data presented within the 'Discover Recipes' view. Ideally the 20 recipe cards would dynamically change as the user makes their filtering choices. 



## Technologies


### Languages
- **[HTML5](https://html.com/html5/)**
- **[CSS3](https://www.w3schools.com/css/)**
- **[Javascript](https://www.javascript.com/)**
- **[Python](https://www.python.org/)**
- **[Jinja2](https://jinja.palletsprojects.com/)** (templating language)


### MongoDB & Dataset
This app uses [MongoDB's](https://www.mongodb.com/cloud/atlas) cloud atlas. 
Where I have deployed a database with five collections, four of which are serving this app. 
MongoDB is a cross-platform document-oriented database. The shared instance of which is hosted on AWS. 

The following methods are in use:
- [db.collection.aggregate()](https://docs.mongodb.com/manual/reference/method/db.collection.aggregate/)
- [db.collection.find()](https://docs.mongodb.com/manual/reference/method/db.collection.find/)
- [db.collection.find_one()](https://docs.mongodb.com/manual/reference/method/db.collection.findOne/)
- [db.collection.insert()](https://docs.mongodb.com/manual/reference/method/db.collection.insert/)
- [db.collection.insert_one()](https://docs.mongodb.com/manual/reference/method/db.collection.insertOne/)
- [db.collection.update()](https://docs.mongodb.com/manual/reference/method/db.collection.update/)
- [db.collection.update_one()](https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/)
- [db.collection.remove()](https://docs.mongodb.com/manual/reference/method/db.collection.remove/)


For this project I used a dataset as I could not locate a suitable api with rich content (for free). 

I located the [following and very extensive dataset](https://archive.org/download/recipes-en-201706/) - containing gigabytes of recipes! Using just the BBC recipes, which contain over 10,000 recipes. 
This was uploaded to MongoDB and then aggregated and a new collection was created from the filtered data. 

I wrote a script to achieve this, json_import.py 
(which should only be run once!). 
It performs the following:
- It reads the JSON recipe data file from archive.org.
- Iterates through it, storing the pairs as a list. 
- isinstance() checks if the data is a list. 
- insert_many() inserts the data to the recipe collection.
- aggregate() is filtering this collection for the following:
  - Finds 'photo_url', check if it exists and the value is not null.
  - It checks that the total_cooking_time is greater than 0 minutes.
  - And that the description exists, using the $expr operator an expression is formed to check that the character length of the description has a greater character length than 80. 
- The results are then made into a new collection using $out. As the collection does not exist a new one will be created. 


### Frameworks (back-end)

- **[Flask](https://flask.palletsprojects.com/)**
  > A python micro web framework


### Dependencies

The following are used in this app:
- **[click](https://pypi.org/project/click/)**
- **[dnspython](https://pypi.org/project/dnspython/)**
- **[Flask](https://pypi.org/project/flask/)**
- **[Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)**
- **[itsdangerous](https://pypi.org/project/itsdangerous/)**
- **[pymongo](https://pypi.org/project/pymongo/)**
- **[Werkzeug](https://pypi.org/project/Werkzeug/)**

Dependencies are in the repository under requirements.txt. 

- **[Chart.js]**(https://www.chartjs.org/)
Was used to provide graphs on the admin dashboard 

### Version Control & Managment
- [Git](https://git-scm.com/)
- [Github](https://github.com/)

### Other software/ tools Used
- [Adobe XD](https://en.wikipedia.org/wiki/Adobe_InDesign)
- [Gitpod](https://gitpod.io)
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
- [Safari Web Development Tools](https://developer.apple.com/safari/tools/)


## Deployment

#### Fork
1. [Login](https://github.com/login) to your GitHub account([or join](https://github.com/join)).
2. Go to the repo by clicking [here](https://github.com/asdub/5km-parks-MP2).
3. Click fork in the top right corner of the screen. 

#### Clone (Locally)
1. [Login](https://github.com/login) to your GitHub account([or join](https://github.com/join)).
2. Go to the repo by clicking [here](https://github.com/asdub/5km-parks-MP2).
3. On the main page of the repository click on 'Code'. 
4. Click on the 'Clipboard'/ copy the clone URL (Clone with HTTPs). 
4. In your local environment open your terminal, navigate to or create a directory.
5. Paste the URL into your terminal and enter. The repo should be successfully cloned.  

#### Deploy on Heroku
Deploying the app on heroku is very straight forward. 

You need to make sure the following files are in the repo you wish to deploy: 
1. requirements.txt 
  > If not, you can create this by opening your terminal, make sure you are in the apps main folder and typing the following command:
      ```
      pip freeze --local > requirements.txt
      ```
  > It creates the txt file in the working directory (where it belongs).

2. Procfile, this tells Heroku to start your app. 
  > You can create one by typing the following into your terminal:
  ```
  echo "web: python app.py" > Procfile
  ```

Once certain those files are present. Go to [Heroku](https://dashboard.heroku.com/) and login or create an account. 

1. Click on 'new' in the top right corner and then create app. 
2. Choose a name and select your region 
3. Your app overview will load. Click on 'Deploy' 
4. Select Github under the deployment method and follow the auth instructions. 
5. Select the repo you wish to use. 
6. In the top ribbon menu select settings then 'Reveal Vars', halfway down the page. 
7. You will need to enter and save the following key/ values: 
    - "IP" : "0.0.0.0"
    - "PORT" : "5000"
    - "SECRET_KEY" : "pick your own"
      (Required by Werkzeug for the password hashing)
8. Go back to 'Deploy' and enable automatic deploys.
9. Below you can click the 'Deploy Branch' button. 
10. Once the app loads click the 'View' button to see your live app. 



## Testing

#### [W3C HTML Validator](https://validator.w3.org/nu/?doc=http%3A%2F%2Flaughing-cookbook.herokuapp.com%2Frecipes) *(Results)*
The W3C validator found 3 initial issues:
1. Warning: Section lacks heading. (line 42) [x]
2. Error: Element span not allowed as child of element ul in this context. (line 603) [x]
3. Error: Stray end tag div. (line 619) [x]


#### [JS Hint](https://jshint.com/)
JS Hint found 1 initial issues:
1. *Warning* Unnecessary semicolon. (line 63) [x]

#### [PEP8 Checker](http://pep8online.com/)
Found 2 initial PEP8 issues:
1. *Warning* E501	line too long (86 > 79 characters). (line 31) [x]
2. *Warning* E129	continuation line under-indented for visual indent. (line 223) [x]

#### [WC3 CSS Validator](https://jigsaw.w3.org/css-validator/validator?uri=http%3A%2F%2Flaughing-cookbook.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors) *(Results)*
WC3 CSS Validator found 1 error & 38 warnings:
1. *Error* & *Warnings* relate to external stylesheets  [ ]

### Google Lighthouse

#### Initial Test
![Lighthouse Results](https://github.com/asdub/laughing-cookbook/blob/master/readme/screenshots/lighthouse_initial.png "Lighthouse Results")

**Best Practices**\
Issues reported, 
  - Serve images in next-gen format
  - Eliminate render-blocking resources
  - Efficiently encode images
  - Remove unused JavaScript
  - Remove unused CSS
  - Enable text compression

**Accessibility**\
Issues reported, 
  - Background and foreground colors do not have a sufficient contrast ratio.
  - Heading elements are not in a sequentially-descending order
  - Links do not have a discernible name

**Best Practices**\
Issues reported, 
  - Does not use HTTPS

**SEO**\
Issues reported, 
  - Document does not have a meta description


#### Steps taken 
1. [Accessibility]Darkened orange to increase contrast ratio[x]
2. [Accessibility]Corrected heading element out of sequence [x]
3. [Accessibility]Aria label added to mobile menu icon [x]
4. [SEO] Added meta tags [x]


#### Re Test
![Lighthouse Results](https://github.com/asdub/laughing-cookbook/blob/master/readme/screenshots/lighthouse_retest.png "Lighthouse Results")

**Performance**\
No performance increases. How the app renders images will need to be actioned on a future update. 

**Accessibility**\
I tried to ensure good contrast between colours. 
Lighthouse has picked up on some of the funner colours as not having sufficient contrast ratio. 

**Best Practices**\
HTTPS is not un use which is lowering this score. 
\
I tried deploying ssl certs via letsencrypt certbot. However, a paid subscription is required on Heroku to use SSL.  

**SEO**\
The SEO score increase to 100 with the addition correct meta tags. 
[Thank you! Heymeta ](https://www.heymeta.com/ )


## Manual Testing 

### Testing Documentation
Testing documentation can be found [here](https://github.com/asdub/laughing-cookbook/blob/master/readme/test/TESTME.md)

### User Stories testing
