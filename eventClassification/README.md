## Event Classification

The classify.py file is used along with the words.csv and events.csv file. The purpose of this code is to tag each event with its event type. If a word from the words.csv file is seen in the event's description or title, that event gets the word's event tags.

When classify.py is ran with python3, metapy, events.csv, and the ranked words.csv it will output the file taged_events.csv. This file will be vital in creating recommendations for users. 
