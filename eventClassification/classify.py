import csv
import metapy

from Utils.utils import parse_doc


def write_classifications():
    event_file = open('../events.csv', 'r')
    event_reader = csv.DictReader(event_file)

    tag_file = open('taged_events.csv', 'w+')
    headers = ['doc_id', 'title', 'url', 'event_type', 'sponsor', 'location', 'date', 'speaker', 'views',
               'originating_calendar', 'topics', 'cost', 'contact', 'e-mail', 'phone', 'registration',
               'description', 'seminars', 'workshops', 'job_networking', 'workouts', 'social_events', 'arts']
    fieldnames = ['seminars', 'workshops', 'job_networking', 'workouts', 'social_events', 'arts']

    tag_writer = csv.DictWriter(tag_file, headers)
    tag_writer.writeheader()

    for event in event_reader:
        word_file = open('words.csv', 'r')
        word_reader = csv.DictReader(word_file)

        # add new feilds
        for tag in fieldnames:
            if tag not in event:
                event[tag] = 0

        doc = metapy.index.Document()
        doc.content("{} {}".format(event['description'].strip().replace("\n", " ").replace("     ", " "), event['title']))
        tokens = list(parse_doc(doc))
        for word_line in word_reader:
            # print(word_line)
            if word_line['word'] in tokens:
                for tag in fieldnames:
                    event[tag] += int(word_line[tag])
        tag_writer.writerow(event)


def classify_doc(csv_file, word_file):
    wordFile = open(word_file, 'r')
    wordRead = csv.DictReader(wordFile)
    with open(csv_file, "w+") as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = ['Seminars', 'Workshops', 'Job Networking', 'Workouts', 'Social events', 'Arts']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        for row in reader:
            print(row)
            for row1 in wordRead:
                if row['description'].find(row1['word']) or row['title'].find(row1['word']):
                    # mark the columns that are 1 in row1, as 1 in row
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
    write_classifications()
    # document = classify_doc('events.csv', 'words.csv')
