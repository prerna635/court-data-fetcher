# log_queries.py
import sqlite3
from datetime import datetime

def log_query(cnr_number):
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cnr TEXT,
            timestamp TEXT
        )
    ''')
    c.execute('INSERT INTO queries (cnr, timestamp) VALUES (?, ?)', (cnr_number, datetime.now()))
    conn.commit()
    conn.close()
