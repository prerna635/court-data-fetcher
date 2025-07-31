from flask import Flask, render_template, request
import sqlite3
import datetime

app = Flask(__name__)

# Dummy scraper function (simulate real scraping)
def fetch_case_data(case_type, case_number, year):
    # Simulated scraped data for demonstration
    return {
        'parties': 'A vs B',
        'filing_date': '2023-01-01',
        'next_hearing': '2024-08-01',
        'latest_order': 'https://example.com/sample_order.pdf'
    }

# Function to log query and result in SQLite database
def log_to_db(case_type, case_number, year, response):
    conn = sqlite3.connect('case_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS case_logs 
                 (id INTEGER PRIMARY KEY, case_type TEXT, case_number TEXT, year TEXT, response TEXT, timestamp TEXT)''')
    c.execute('INSERT INTO case_logs (case_type, case_number, year, response, timestamp) VALUES (?, ?, ?, ?, ?)',
              (case_type, case_number, year, str(response), str(datetime.datetime.now())))
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        case_type = request.form['case_type']
        case_number = request.form['case_number']
        year = request.form['year']
        data = fetch_case_data(case_type, case_number, year)
        log_to_db(case_type, case_number, year, data)
        return render_template('result.html', data=data)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

