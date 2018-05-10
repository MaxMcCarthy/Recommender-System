events = {}
metadata = {}

import csv
with open('taged_events_no_duplicates.csv', newline='\n') as csv_file:
    eventsreader = csv.reader(csv_file, delimiter=',')
    header = next(eventsreader)
    types = header[-6:]
    for t in types: 
        events[t] = set()
    for row in eventsreader: 
        categories = row[-6:]
        url = row[2]
        metadata[url] = list(zip(header, row))
        for idx, cat in enumerate(categories): 
            if cat != "0":
                events[types[idx]].add(url)
                
               
def recommend(survey_categories):
    sets = []
    for cat in survey_categories: 
        sets.append(events[cat])
        
    all_urls = set.intersection(*sets)
    all_events = []
    for url in all_urls: 
        all_events.append(metadata[url])

    return all_events

