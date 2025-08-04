# ⚖️ Court-Data Fetcher & Mini-Dashboard

This project is a Flask-based web application that allows users to **fetch and view real-time Indian court case metadata** using a **CNR number**.  
It scrapes data directly from the [eCourts portal](https://services.ecourts.gov.in/ecourtindia_v6/) using **Selenium** and solves **CAPTCHAs automatically using OCR (Tesseract)**.

---

## 📌 Features

- 🔎 **Search case details** using just the CNR number
- 🧠 **Auto-solves CAPTCHA** using Tesseract OCR
- 🧾 Parses and displays key metadata (filing date, parties, status, etc.)
- 💾 Stores previously searched CNRs in an **SQLite database**
- ❗ Error handling for invalid/missing inputs
- 📊 Clean, responsive UI with Flask + HTML/CSS

---

## 🖼️ Sample UI

<img src="static/court.png" alt="UI Preview" width="500">

---

## 🚀 How It Works

1. User enters a valid CNR number (e.g., MHSV020000002021)
2. Selenium opens the eCourts portal and fills the form
3. CAPTCHA is solved using pytesseract (OCR)
4. Scraped data is parsed and shown on the result page
5. CNR search is logged in SQLite

---

## 🧠 Tech Stack

- Python (Flask, Selenium, pytesseract)
- HTML5, CSS3 (Bootstrap)
- SQLite (for query logging)
- ChromeDriver (headless scraping)
- eCourts Portal (Target site)

---

## 🛠️ Installation

### ✅ Prerequisites:
- Python 3.x
- Google Chrome
- ChromeDriver (v114 for compatibility)
- Tesseract OCR (Install and add to PATH)


