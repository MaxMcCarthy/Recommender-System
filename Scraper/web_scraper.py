from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import csv


# with help from:
# https://realpython.com/python-web-scraping-practical-introduction/


def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        print('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns true if the response seems to be HTML, false otherwise
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def scrape_academic():
    headings = ['CS', 'STAT', 'LAS', 'ENG', 'GRAD']
    urls = ['http://calendars.illinois.edu/list/504', 'https://calendars.illinois.edu/list/1439',
            "http://calendars.illinois.edu/list/1249", 'http://calendars.illinois.edu/list/2568',
            'http://calendars.illinois.edu/list/3695']

    count = 0
    for url in urls:
        base_url = 'http://calendars.illinois.edu'
        html = simple_get(url)
        html = BeautifulSoup(html, 'html.parser')
        for p in html.select('ul'):
            for h3 in p.select('h3'):
                for a in h3.select('a'):
                    print(a['href'])
                    print(a.text)
                    print('')
                    event = simple_get(base_url + a['href'])
                    event = BeautifulSoup(event, 'html.parser')
                    for dd in event.findAll("section", {"class": "detail-content"}):
                        for desc, info in zip(dd.select('dt'), dd.select('dd')):
                            print("{} : {}\n".format(desc.text, info.text))
                        for summary in dd.findAll('dd', {"class": 'ws-description'}):
                            print(summary.text.strip())
                    print('\n\n\n')
                    print(count)
                    count += 1


def scrape_arc():
    urls = ['http://calendars.illinois.edu/list/7']

    count = 0
    for url in urls:
        base_url = 'http://calendars.illinois.edu'
        html = simple_get(url)
        html = BeautifulSoup(html, 'html.parser')
        for p in html.select('ul'):
            for h3 in p.select('h3'):
                for a in h3.select('a'):
                    print(a['href'])
                    print(a.text)
                    print('')
                    event = simple_get(base_url + a['href'])
                    event = BeautifulSoup(event, 'html.parser')
                    for dd in event.findAll("section", {"class": "detail-content"}):
                        for desc, info in zip(dd.select('dt'), dd.select('dd')):
                            print("{} : {}\n".format(desc.text, info.text))
                        for summary in dd.findAll('dd', {"class": 'ws-description'}):
                            print(summary.text.strip())
                    print('\n\n\n')
                    print(count)
                    count += 1


def scrape_url(urls):
    count = 0
    with open('events.csv', 'a+') as csvfile:
        headers = ['doc_id', 'title', 'url', 'event_type', 'sponsor', 'location', 'date', 'speaker', 'views',
                   'originating_calendar', 'topics', 'cost', 'contact', 'e-mail', 'phone', 'registration',
                   'description']
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        base_url = 'http://calendars.illinois.edu'
        for url in urls:
            html = simple_get(url)
            html = BeautifulSoup(html, 'html.parser')
            for p in html.select('ul'):
                for h3 in p.select('h3'):
                    row = {'doc_id': 'NA', 'title': 'NA', 'url': 'NA', 'event_type': 'NA', 'sponsor': 'NA',
                           'location': 'NA', 'date': 'NA', 'speaker': 'NA', 'views': 'NA',
                           'originating_calendar': 'NA', 'topics': 'NA', 'cost': 'NA', 'contact': 'NA', 'e-mail': 'NA',
                           'phone': 'NA', 'registration': 'NA', 'description': 'NA'}
                    for a in h3.select('a'):
                        row['doc_id'] = count
                        row['title'] = a.text
                        row['url'] = base_url + a['href']
                        event = simple_get(base_url + a['href'])
                        event = BeautifulSoup(event, 'html.parser')
                        for dd in event.findAll("section", {"class": "detail-content"}):
                            for desc, info in zip(dd.select('dt'), dd.select('dd')):
                                # print("{} : {}\n".format(desc.text, info.text))
                                name = desc.text.lower().strip().replace(" ", "_")
                                if name == 'topic':
                                    name += 's'
                                row[name] = info.text
                            description = ''
                            for summary in dd.findAll('dd', {"class": 'ws-description'}):
                                description += summary.text.strip()
                                # print(summary.text.strip())
                            if description != '':
                                row['description'] = description
                        writer.writerow(row)
                        # print('\n\n\n')
                        print(count)
                        count += 1


if __name__ == '__main__':
    # optional smaller calendars
    # scrape_academic()
    fitness_classes = 'https://calendars.illinois.edu/list/4046'
    krannert_perf = 'https://calendars.illinois.edu/list/33'
    campus_rec = 'http://calendars.illinois.edu/list/2628'
    student_affairs = 'http://calendars.illinois.edu/list/1771'
    master = 'http://calendars.illinois.edu/list/7'

    scrape_url([fitness_classes, krannert_perf, campus_rec, student_affairs, master])
    # scrape_url(krannert_perf)
    # scrape_url(campus_rec)
    # scrape_url(student_affairs)
    # scrape_url(master)
