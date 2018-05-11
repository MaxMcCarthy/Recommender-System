# Utils

The utils.py was used to find the most common words in the title or description of events from the events.csv file. The csv file was read in and duplicated events were removed.

This file was ran outside of the main.py file to find the most common words from the events.csv file. This file can be run with python3 and the metapy class. To run the utils.py file, make sure to have the events.csv file in the same directory as well as the lemur-stopwords.txt file. The utils.py will output a words.csv file with all of the word and word counts of the words from the title and description in events.csv. 

Once the top words were found, the top 100 words were sorted through and tagged as an event type. Each word was search in the events.csv file to see the relevance of the word. Non-relevant words were removed. This left us 40 words which can be seen with their tags in words.csv. 

Finally, the words were added to the database using the populate_db.py script. 
