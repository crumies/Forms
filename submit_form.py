from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# User credentials and form URL from environment variables
google_username = os.getenv('GOOGLE_USERNAME')
google_password = os.getenv('GOOGLE_PASSWORD')
form_url = 'https://docs.google.com/forms/u/1/d/e/1FAIpQLSf5QHYs-VQOiO8ceCQcJRFNfaOAXPBETVfxvKpi4bVWT9YV7A/viewform'

# Initialize WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Function to log in to Google
def login_to_google():
    driver.get('https://accounts.google.com/')

    # Input email
    email_field = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    email_field.send_keys(google_username)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)

    # Input password
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    password_field.send_keys(google_password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

# Function to fill and submit the form
def submit_form():
    driver.get(form_url)
    time.sleep(3)  # Wait for the form to load

    # Check the checkbox (assuming there's only one)
    checkbox = driver.find_element(By.CSS_SELECTOR, 'div[role="checkbox"]')
    checkbox.click()
    time.sleep(1)

    # Submit the form
    submit_button = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-label="Submit"]')
    submit_button.click()
    time.sleep(2)

# Main script
try:
    login_to_google()

    while True:
        submit_form()
        time.sleep(5)  # Wait before resubmitting (modify as needed)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
