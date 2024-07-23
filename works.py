from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver (assuming you're using Chrome)
options = Options()
options.headless = False  # Set to True if you want to run headless
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://www.sharesansar.com/today-share-price")

# Wait until the date picker input field is present
date_picker = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "fromdate"))
)

# Use JavaScript to set the value of the date picker
new_date = "2022-07-20"
driver.execute_script("arguments[0].value = arguments[1]; arguments[0].dispatchEvent(new Event('change'));", date_picker, new_date)

# Wait until the search button is clickable
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btn_todayshareprice_submit"))
)

# Click the search button
search_button.click()

# Allow some time to observe the result
time.sleep(5)

# Close the browser
driver.quit()
