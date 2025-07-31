import requests
from bs4 import BeautifulSoup

def fetch_case_data(case_type, case_number, year):
    url = "https://services.ecourts.gov.in/ecourtindia_v6/"
    
    payload = {
        "stateCode": "HR",
        "distCode": "FBD",
        "caseType": case_type,
        "caseNo": case_number,
        "caseYear": year
    }

    session = requests.Session()
    response = session.post(url, data=payload)
    soup = BeautifulSoup(response.text, "html.parser")

    # Sample parsing logic – adjust to match actual HTML structure
    petitioner = soup.find("td", text="Petitioner").find_next("td").text.strip()
    respondent = soup.find("td", text="Respondent").find_next("td").text.strip()
    filing_date = soup.find("td", text="Filing Date").find_next("td").text.strip()
    next_hearing = soup.find("td", text="Next Hearing Date").find_next("td").text.strip()
    pdf_url = soup.find("a", text="View Order")["href"]

    return {
        "petitioner": petitioner,
        "respondent": respondent,
        "filing_date": filing_date,
        "next_hearing": next_hearing,
        "pdf_url": pdf_url
    }, response.text
