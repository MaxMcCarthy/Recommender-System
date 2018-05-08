import csv

def classify_doc(csv_file, word_file):
    wordFile = open(word_file, 'r')
    wordRead = csv.DictReader(wordFile)
    	
    with open(csv_file, "+") as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = ['Seminars', 'Workshops', 'Job Networking','Workouts', 'Social events','Arts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for row in reader:
        	for row1 in wordRead:
        		if row['description'].find(row1['word']) or row['title'].find(row1['word']):
        			#mark the columns that are 1 in row1, as 1 in row 
        			if row1['Seminars'].find('1'):
        				writer.writerow({'Seminars': '1'})
        			if row1['Workshops'].find('1'):
        				writer.writerow({'Workshops': '1'})
        			if row1['Job Networking'].find('1'):
        				writer.writerow({'Job Networking': '1'})
        			if row1['Workouts'].find('1'):
        		        	writer.writerow({'Workouts': '1'})
        			if row1['Arts'].find('1'):
        		        	writer.writerow({'Arts': '1'})
        			if row1['Social events'].find('1'):
        			        writer.writerow({'Social events': '1'})
    return 0


if __name__ == '__main__':
    document = classify_doc('events.csv','words.csv')
