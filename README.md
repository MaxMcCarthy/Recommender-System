# Recommender System

## Overview

This web application's main purpose is to recommend events in and around Urbana-Champaign to the public. It utilizes multiple existing calendars at UIUC to recommend events in accordance to the user's major, college and hobbies.

The user can login to their existing account or sign up and create a new account with an email address and a password. If the user signs up and creates a new account, they fill out a survey with information about their college, possible secondary college, academic standing or degree level, and any other specific activities that represent their interests. The information in the survey is used to determine what activities or events will be recommended to the user. Afterwards, the user will be provided with a list of recommended events that the user likely will find relevant or interesting. If the user logs in, the user will also find the list of recommended events.


## Project Contents

* Config - Contains the configuration for the database that allows the database instance to be used by all files in the project.
* Forms - A collection of Flask Form Classes that are used to collect and validate user input. 
* Recommender - ___
* Scraper - This contains files that use the beautifulsoup4 package to scrape university webpages and gather upcoming events.
* Utils - This file contains general utilities that take a document, stem it, and write to a CSV file with the counts of each word in all of the documents. From here, we selected the most popular 40 words (removing useless words like Illinois and event"). These 40 words were each associated with 1 tag from \['seminars', 'workshops', 'job_networking', 'workouts', 'social_events', 'arts'\]. There is also a file that helps populate the database from a CSV file of events.
* bagOfWords - This folder contains the original python script to find the top words from the events.csv file. This code was later updated to what is seen in the Utils folder. 
* database - This file contains the python and SQL needed to create the database.
* eventClassification - This contains a file that takes the events, reads all of the words in the description, and checks to see if any of the words are in the 40 key words. If there are any, the document is assigned the appropriate tag from \['seminars', 'workshops', 'job_networking', 'workouts', 'social_events', 'arts'\].
* static - Contains any static elements for the webpage including the CSS file and images
* templates - Contains all website (HTML) files.
* events.csv - This contains the events scraped from university webpages. They lack tags.
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

Max: I wrote the Flask backend that powers our web application. I then wrote the server code that renders the HTML, processes POST requests from the web app, makes database queries, and sends results to the user. I also created Flask From Classes that recieve the user data, validate it, and prevent CSRF Attacks. I added Jinja2 templating to all of the HTML files to allow them to send and recieve data via Flask. I obtained bootstrap samples to create the login page and the signin page and wrote the results page myself.

I designed a webscraper using beautifulsoup4. The scraper looks at several UIUC websites and finds events and writes them out to a CSV file. I assisted in writing code in Utils to get the total count of each word used in our collection. I also assisted in writing code to add the tag fields to the CSV file.

Lastly, I developed an SQL schema for our project. The project actively uses the user table and interests table to log users in and determine which events to display. The database includes support for future development where the scraper will write directly to the database instead of intermediate CSV files.

Lily: I created the system that would go through the event words and figure out the top words describing events from the title and description of the events. After finding the top 100 words, I sorted through these words to find the ones most relevant to the events. From the 100 words, I selected 40 words and tagged them as the six event types. Finally, I created another script to tag the events with their type based on the top 40 words that had been selected and tagged.  

Riya: I created the recommender system using the modified database file so that the web application returns events in the categories the user selected. I built the recommender function along with the different sets that hold the categorized events. 

Raymond: I obtained the initial website from Start Bootstrap and modified it to serve as our structure and platform for the HTML portions of our project. I also created the survey that asks the users for their college, possible secondary college, academic standing or degree level, and any other specific activities that represent their interests. The survey served as our criteria for determining what activities or events to recommend to the user.
