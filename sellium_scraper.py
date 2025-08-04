import requests
from bs4 import BeautifulSoup

def get_case_details(cnr_number, captcha_input):
    session = requests.Session()
    base_url = "https://services.ecourts.gov.in/ecourtindia_v6/"

    # Step 1: Get the main search page to grab cookies
    initial_response = session.get(base_url + "casestatus/cnr-search.php")
    
    # Step 2: Prepare the payload
    payload = {
        "cnrno": cnr_number,
        "captcha": captcha_input,
        "submit": "Search"
    }

    # Step 3: Send POST request
    search_url = base_url + "casestatus/cnr-search.php"
    headers = {
        "Referer": search_url,
        "User-Agent": "Mozilla/5.0"
    }
    
    response = session.post(search_url, data=payload, headers=headers)

    soup = BeautifulSoup(response.content, "html.parser")
    case_info = soup.find("div", {"class": "case_details_table"})

    if case_info:
        return case_info.prettify()
    else:
        return "<p>❌ Case not found or CAPTCHA incorrect. Please try again.</p>"

