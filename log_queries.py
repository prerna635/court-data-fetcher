import sqlite3
from datetime import datetime

def log_query(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect('query_logs.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            timestamp TEXT,
            raw_response TEXT
        )
    ''')
    
    c.execute('''
        INSERT INTO logs (case_type, case_number, filing_year, timestamp, raw_response)
        VALUES (?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), raw_response))
    
    conn.commit()
    conn.close()
