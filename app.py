from flask import Flask, render_template, request
from scraper import get_case_details

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch', methods=['POST'])
def fetch():
    cnr = request.form['cnr']
    captcha = request.form['captcha']
    
    result = get_case_details(cnr, captcha)
    return render_template('result.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
