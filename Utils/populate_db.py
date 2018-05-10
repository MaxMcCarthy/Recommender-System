import csv
import metapy

from Utils.utils import parse_doc
from Config.config import db


words = ['research',
         'exhibit',
         'art',
         'music',
         'work',
         'write',
         'scienc',
         'program',
         'yoga',
         'symposium',
         'graduat',
         'tour',
         'servic',
         'engin',
         'market',
         'talk',
         'perform',
         'societ',
         'workshop',
         'solar',
         'folk',
         'project',
         'krannert',
         'ncsa',
         'museum',
         'system',
         'retreat',
         'book',
         'artist',
         'band',
         'fair',
         'allerton',
         'onlin',
         'bike',
         'agricultur',
         'energi',
         'convers',
         'jazz',
         'practic']


def get_word_counts(document):
    counts = []
    doc = metapy.index.Document()
    doc.content(document)
    tokens = list(parse_doc(doc))
    for word in words:
        counts.append(tokens.count(word))
    return counts

# 54

def populate_documents():
    with open('../events.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        column_names = words.copy()
        column_names[4] += '_'
        column_names[5] += '_'
        for row in reader:
            doc_id = row['doc_id']
            word_count = get_word_counts(row['description'])
            sql = "INSERT INTO documents (doc_id, {0}, title, url, event_type, sponsor, location, date_, speaker, originating_calendar, topics, cost, contact, email, phone, registration) values ({1})".format(', '.join(column_names), ','.join(['?']*54))
            print(sql)
            cur = db.cursor()
            params = (doc_id, ) + tuple(word_count) + (row['title'], row['url'], row['event_type'], row['sponsor'], row['location'], row['date'], row['speaker'], row['originating_calendar'],
                                                       row['topics'], row['cost'], row['contact'], row['e-mail'], row['phone'], row['registration'])
            cur.execute(sql, params)
            db.commit()


def populate_events():
    print(db)
    with open('../taged_events_no_duplicates.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        cur = db.cursor()
        for row in reader:
            sql = '''INSERT INTO events
                    (doc_id,title,url,event_type,sponsor,location,date_,speaker,originating_calendar,topics,cost,contact,e_mail,phone,registration,description,seminars,workshops,job_networking,workouts,social_events,arts)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            params = (row['doc_id'], row['title'], row['url'], row['event_type'], row['sponsor'], row['location'], row['date'], row['speaker'], row['originating_calendar'],
                                    row['topics'], row['cost'], row['contact'], row['e-mail'], row['phone'], row['registration'], row['description'], row['seminars'], row['workshops'],
                      row['job_networking'], row['workouts'], row['social_events'], row['arts'])
            cur.execute(sql, params)
    db.commit()


if __name__ == '__main__':
    # populate_documents()
    populate_events()