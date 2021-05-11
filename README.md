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

* [User Experience (UX)](#user-experience-(ux))
    * [Brief](#Brief)
    * [Project Aims](#the-aim-of-this-project-is-to)
    * [User Stories](#new-user-stories)
* [Design](#design)
    * [Frameworks](#frameworks)
    * [Colours](#colours)
    * [Wireframes](#wireframes)
    * [Typography](#typography)
    * [Iconography](#iconography)
    * [App Flow](#appflow)
    * [Responsive](#responsive)
    * [Features](#features)
    * [Database Design](#databasedesign)
    * [Future Features](#future-features)
* [Technologies](#technologies)
    * [Languages](#languages)
    * [MongoDB](#mongodb)
    * [APIs & Data](#apidata)
    * [Version Control & Managment](#version-control--managment)
    * [Software/ Tools Used](#other-software-tools-used)
* [Deployment](#deployment)
    * [Heroku](#heroku)
    * [Fork](#fork)
    * [Clone (Locally)](#clone-locally)
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
The [Materialize](https://materializecss.com/) front-end framework was used to style this app. 


### Colours 
A limited palette of colours was used throughout the app.\n
As the app contains dynamically loaded imagery I thought it best to limit the use of colours to avoid potential colour clashing. 

**There are six colours used in total throughout the app.**\n

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

Wireframes can be viewed in full resolution ![here on Adobe XD](![Wireframes](https://xd.adobe.com/view/07051529-26a9-46df-84cf-76d5c9ea2a4e-5256/ "Wireframes")
).
