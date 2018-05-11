# bagOfWords

This was the initial method used to find the most common words in the events.csv file. This method was NOT used in the end to find the most common words. The bag of words method in the utils folder was used instead. 

This folder contains the information about finding the 25 most common words. 

The config folder holds the analyzer types used. The bagOfWordsAttempt1.py includes the code to create the bag of words. The metapy class was used to find the common words. 

The categories used to find this are "title" "sponser" and "topic" from the events.csv file. The text from these categories was put into the words.txt file. 

Please see stop words for additional removed words from finding top 25 words. The words added are above the symbols in this file. 

The output is: ['art', 'american', 'music', 'exhibit', 'archiv', 'recreat', 'museum', 'agricultur', 'studi', 'krannert', 'farm', 'tour', 'spurlock', 'work', 'cultur', 'yoga', 'kam', 'orchestra', 'outreach', 'communic', 'unexpect', 'birthday', 'establish', 'water', 'adventur']

To generate the above 25 words run the bagOfWordsAttempt1.py file (use python3) with everything else seen in this folder. If not installed, install the python package metapy as well. 
