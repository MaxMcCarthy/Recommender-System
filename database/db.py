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


def init_user_table(conn):
    cur = conn.cursor()
    sql = '''
        CREATE TABLE IF NOT EXISTS user (
        user_id  INTEGER        PRIMARY KEY AUTOINCREMENT,
        email STRING (3, 20) NOT NULL,
        password STRING (3, 20) NOT NULL
        );
    '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
