import csv
import metapy

from Utils.utils import parse_doc
from config.config import db


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


if __name__ == '__main__':
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
