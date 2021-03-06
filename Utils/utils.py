import csv
import metapy


def remove_duplicates_from_csv():
    headers = ['doc_id', 'title', 'url', 'event_type', 'sponsor', 'location', 'date', 'speaker', 'views',
               'originating_calendar', 'topics', 'cost', 'contact', 'e-mail', 'phone', 'registration',
               'description', 'seminars', 'workshops', 'job_networking', 'workouts', 'social_events', 'arts']

    tag_file = open('taged_events_no_duplicates.csv', 'w+')

    writer = csv.DictWriter(tag_file, headers)
    writer.writeheader()
    seen = {}
    with open('/Users/Max/PycharmProjects/Recommender-System/Config/taged_events.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['title'] not in seen:
                seen[row['title']] = True
                writer.writerow(row)


def generate_doc(csv_file):
    document = ''
    title_list = {}
    with open(csv_file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['title'] not in title_list:
                title_list[row['title']] = True
                if row['description'] != 'NA':
                    document += ' ' + row['description']
                if row['title'] != 'NA':
                    document += ' ' + row['title']
    return document


def parse_doc(doc):

    tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)

    tok.set_content(doc.content())

    tok1 = metapy.analyzers.LowercaseFilter(tok)
    tok1.set_content(doc.content())

    tok2 = metapy.analyzers.ListFilter(tok1, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
    tok2.set_content(doc.content())

    tok3 = metapy.analyzers.Porter2Filter(tok2)
    tok3.set_content(doc.content())

    return tok3


def get_word_counts(tokens):
    words = {}
    for token in tokens:
        print(token)
        if token != '<s>' and token != '</s>':
            if token not in words:
                words[token] = 0
            words[token] += 1

    sorted_words = [{'word': key, 'count': value} for key, value in sorted(words.items(), key=lambda x: x[1], reverse=True)]

    return sorted_words


if __name__ == '__main__':
    # remove_duplicates_from_csv()
    document = generate_doc('events.csv')
    doc = metapy.index.Document()
    doc.content(document)
    tokens = parse_doc(doc)
    sorted_words = get_word_counts(tokens)
    with open('words.csv', 'w+') as csvfile:
        fieldnames = ['word', 'count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sorted_words)
