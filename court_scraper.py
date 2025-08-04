from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import time
import os

def fetch_court_data(cnr_number):
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")

        #  Manually specify Chrome browser binary location
        chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # <-- Update this path if yours is different

        #  Path to your ChromeDriver
        chrome_driver_path = "C:/Users/prern/OneDrive/Desktop/projects/court data fetcher/chromedriver.exe"
        service = Service(chrome_driver_path)

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

        # Switch to iframe with form
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "contentAreaFrame")))

        cnr_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "cnrno")))
        cnr_input.clear()
        cnr_input.send_keys(cnr_number)

        captcha_img = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "captcha_image")))
        captcha_path = os.path.join(os.getcwd(), "captcha.png")
        captcha_img.screenshot(captcha_path)

        captcha_text = pytesseract.image_to_string(Image.open(captcha_path)).strip()
        print(f"[OCR Captcha]: {captcha_text}")

        captcha_input = driver.find_element(By.ID, "captcha")
        captcha_input.clear()
        captcha_input.send_keys(captcha_text)

        driver.find_element(By.ID, "submit").click()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "ecourts_case_status")))
        result_div = driver.find_element(By.ID, "ecourts_case_status")
        case_result = result_div.text.strip()

        return {
            "CNR": cnr_number,
            "Result": case_result
        }

    except Exception as e:
        return f"Failed to fetch court data: {str(e)}"
    
    finally:
        if driver:
            driver.quit()
