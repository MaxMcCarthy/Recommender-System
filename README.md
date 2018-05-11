# Recommender System

## Overview

This web application's main purpose is to recommend events in and around Urbana-Champaign to the public. It utilizes multiple existing calendars at UIUC to recommend events in accordance to the user's major, college and hobbies.

The user can login to their existing account or sign up and create a new account with an email address and a password. If the user signs up and creates a new account, they fill out a survey with information about their college, possible secondary college, academic standing or degree level, and any other specific activities that represent their interests. The information in the survey is used to determine what activities or events will be recommended to the user. Afterwards, the user will be provided with a list of recommended events that the user likely will find relevant or interesting. If the user logs in, the user will also find the list of recommended events.


## Project Contents

* Config - Contains the configuration for the database that allows the database instance to be used by all files in the project.
* Forms - A collection of Flask Form Classes that are used to collect and validate user input. 
* Recommender - ___
* Scraper - This contains files that use the beautifulsoup4 package to scrape university webpages and gather upcoming events.
* Utils - This file contains general 
* bagOfWords - ___
* database - ___
* eventClassification - ___
* static - Contains any static elements for the webpage including the CSS file and images
* templates - Contains all website (HTML) files
* events.csv - ___
* main.py - This is the main function for the application. It contains all of the flask code the powers the web app.
* requirements.txt - A text file detailing the package requirements of the project. Run "pip3 install -r requirements.txt" to get all of the requirements installed on your computer.
* taged_events_no_duplicates.csv - Final csv file. It contains all the events and their tags. Duplicate events have been removed from this file.


## Software

* Python (version ____)
* Flask (version __)
* Beautiful Soup (version ___)
* metapy (version __)
* __ (other Python extensions/libraries)
* HTML (version ____)


## Contributions

Max: ____

Lily: _____

Riya: I created the recommender system using the modified database file so that the web application returns events in the categories the user selected. I built the recommender function along with the different sets that hold the categorized events. 

Raymond: I obtained the initial website from Start Bootstrap and modified it to serve as our structure and platform for the HTML portions of our project. I also created the survey that asks the users for their college, possible secondary college, academic standing or degree level, and any other specific activities that represent their interests. The survey served as our criteria for determining what activities or events to recommend to the user.
