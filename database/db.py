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
