import sqlite3
from sqlite3 import Error


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
        init_tables(conn)
        conn.row_factory = dict_factory
        return conn
    except Error as e:
        print(e)
        return None


def init_tables(conn):
    init_user_table(conn)
    init_interests_tables(conn)
    init_document_table(conn)


def init_user_table(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS user (
        user_id  INTEGER        PRIMARY KEY AUTOINCREMENT,
        email STRING (3, 20) NOT NULL,
        password STRING (3, 20) NOT NULL,
        college STRING (1,255),
        secondary_college STRING (1,255),
        degree_level STRING (1,255)
        
        );
    '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def init_interests_tables(conn):
    sql = '''
            CREATE TABLE IF NOT EXISTS interests (
            user_id  INTEGER  PRIMARY KEY,
            seminars BOOLEAN DEFAULT(0),
            workshops BOOLEAN DEFAULT(0),
            job_networking BOOLEAN DEFAULT(0),
            workouts BOOLEAN DEFAULT(0),
            social_events BOOLEAN DEFAULT(0),
            art BOOLEAN DEFAULT(0)
            );
        '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def init_document_table(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS documents (
        doc_id INTEGER PRIMARY KEY,
        research INTEGER DEFAULT(0),
        exhibit INTEGER DEFAULT(0),
        art INTEGER DEFAULT(0),
        music INTEGER DEFAULT(0),
        work_ INTEGER DEFAULT(0),
        write_ INTEGER DEFAULT(0),
        scienc INTEGER DEFAULT(0),
        program INTEGER DEFAULT(0),
        yoga INTEGER DEFAULT(0),
        symposium INTEGER DEFAULT(0),
        graduat INTEGER DEFAULT(0),
        tour INTEGER DEFAULT(0),
        servic INTEGER DEFAULT(0),
        engin INTEGER DEFAULT(0),
        market INTEGER DEFAULT(0),
        talk INTEGER DEFAULT(0),
        perform INTEGER DEFAULT(0),
        societ INTEGER DEFAULT(0),
        workshop INTEGER DEFAULT(0),
        solar INTEGER DEFAULT(0),
        folk INTEGER DEFAULT(0),
        project INTEGER DEFAULT(0),
        krannert INTEGER DEFAULT(0),
        ncsa INTEGER DEFAULT(0),
        museum INTEGER DEFAULT(0),
        system INTEGER DEFAULT(0),
        retreat INTEGER DEFAULT(0),
        book INTEGER DEFAULT(0),
        artist INTEGER DEFAULT(0),
        band INTEGER DEFAULT(0),
        fair INTEGER DEFAULT(0),
        allerton INTEGER DEFAULT(0),
        onlin INTEGER DEFAULT(0),
        bike INTEGER DEFAULT(0),
        agricultur INTEGER DEFAULT(0),
        energi INTEGER DEFAULT(0),
        convers INTEGER DEFAULT(0),
        jazz INTEGER DEFAULT(0),
        practic INTEGER DEFAULT(0),
        title CHAR(255),
        url CHAR(255),
        event_type CHAR(255),
        sponsor CHAR(255),
        location CHAR(255),
        date_ CHAR(255),
        speaker CHAR(255),
        originating_calendar CHAR(255),
        topics CHAR(255),
        cost CHAR(255),
        contact CHAR(255),
        email CHAR(255),
        phone CHAR(255),
        registration CHAR(255)
        );'''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
