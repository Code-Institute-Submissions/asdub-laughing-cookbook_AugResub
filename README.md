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
    * [MongoDB](#mongodb)
    * [Frameworks (back-end)](#frameworks-back-end)
    * [APIs & Data](#apidata)
    * [Version Control & Managment](#version-control--managment)
    * [Software/ Tools Used](#other-software-tools-used)
* [Deployment](#deployment)
    * [Heroku](#heroku)
    * [Fork](#fork)
    * [Clone (Locally)](#clone-locally)
    * [Dependencies](#dependencies)
* [Testing](#testing)
    * [W3C HTML](#wc3-html-validator-results)
    * [JS Hink](#js-hint)
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

Only one font is in use:\n
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

**More in depth informaton on this subject can be found below within the [APIs & Data](#apidata) section below**

I orginally wanted to use an API to provide recipe content for the app. However, this provided impossible to locate without a paid subcription so I opted to used a suitable dataset of recipes instead. . 


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
For the purposes of this app I created a futher collection, recipe_clean containing 1991 recipes (some of which are user submitted). This was to ensure that the data always had the required field values to A) avoid errors and B) ensure content quality. 

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
My view is that this collection would be used for an future site specific variables, perhaps themes or the site content itself. 


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

**Discover Recipes** - *(/recipes)*
- A count of current recipes is provided within the welcome text. 
- Search functionality is provided, a user can search title text, recipe description, and chef name. 
- On load the user will be presented with 20 recipe cards, which are randomised on each page reload. 
  - Each recipe card contains an image, title, description, a pin recipe button (if logged in), the recipes time and a link to *'View Recipe'* to proceed to the recipe page. 
- The user can pin a recipe to their 'My Recipe' profile or click 'View Recipe to see more information (once authorised). 
- An administrator has the ability to edit any recipe from this view. 

**Recipe** - *(/recipe/<recipe_id>)*
- This view gives the user the complete recipe inclusing inredients and instuctions. 
- Under the description, an unauthorised user will see a login button. 
  - If authorised, this button will change to a pin or unpin recipe button.
  - If the user submitted the recipe in view they will have the option to delete and edit. 
  - An administrator can delete and edit any recipe. 
  - Defenisive design is present here, when deleting a recipe a modal will appear to confirm the users choice. 
  - In addition to the recipe related content, advertising content is displayed under the recipes timings. 
    - This content is stored in the advert_data database collection mentioned above. 
    - An administrator can change the active advertiser from the admin dashboard. 

**Add Recipe** - *(/add_recipe)*