from flask import Flask, render_template, request
from court_scraper import fetch_court_data

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        cnr_number = request.form.get("cnr")
        if cnr_number:
            response = fetch_court_data(cnr_number.strip())
            if isinstance(response, dict):
                result = response
            else:
                error = response
        else:
            error = "CNR number cannot be empty."
    return render_template("index_new.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
