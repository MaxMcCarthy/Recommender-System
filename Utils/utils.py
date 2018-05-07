import csv
import metapy

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
    #
    # tok4 = metapy.analyzers.LowercaseFilter(tok3)
    # tok4.set_content(doc.content())

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
