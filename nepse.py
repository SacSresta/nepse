from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Initialize the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.sharesansar.com/today-share-price")

# Find the date picker input field by its ID
date_picker = driver.find_element(By.ID, "fromdate")

# Clear any existing value in the input field
date_picker.clear()

# Input the desired date (e.g., "2022-07-20")
date_picker.send_keys("2022-07-20")

# (Optional) Press Enter to confirm the input
date_picker.send_keys(Keys.RETURN)

# Wait until the search button is clickable
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "btn_todayshareprice_submit"))
)


# Click the search button
search_button.click()

# Allow some time to observe the result
time.sleep(10)

# Close the browser
driver.close()
