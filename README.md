# CS410 Final Project

## Overview

This web application's main purpose is to recommend events in and around Urbana-Champaign to the public. It utilizes multiple existing calendars at UIUC to recommend events in accordance to the user's major, college and hobbies. 

The user can login to their existing account or sign up and create a new account with an email address and a password. If the user signed up and created a new account, they would be directed to a survey where they input information about themselves including their college, possible secondary college, academic standing or degree level, and any other specific activities that represent their interests. The information in the survey is used as our criteria for determining what activities or events will be recommended to the user. Afterwards, the user will be provided with a list of recommended events that the user likely will find relevant or interesting.

_______


## Folder Contents

Config
Forms
Recommender
Scraper
Utils 
bagOfWords
database
eventClassification
static
templates
events.csv
main.py
requirements.txt
taged_events_no_duplicates.csv


## Software

_______


## Contributions

Max: ____
Lily: _____
Riya: I created the recommender system using the modified database file so that the web application returns events in the categories the user selected. I built the recommender function along with the different sets that hold the categorized events. 
Raymond: I created the initial website that served as our structure and platform for the HTML portions of our project. I also created the survey that asks the users for their college, possible secondary college, academic standing or degree level, and any other specific activities that represent their interests. The survey served as our criteria for determining what activities or events to recommend to the user.
