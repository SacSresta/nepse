from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from datetime import datetime.timedelta


# Initialize the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Open the website
driver.get("https://www.sharesansar.com/today-share-price")

# Wait for the table to be present in the DOM
driver.implicitly_wait(10)  # waits up to 10 seconds for elements to be found

# Locate the target div and table
target_div = driver.find_element(By.CLASS_NAME, 'headFixedWrapper')
table = target_div.find_element(By.ID, 'headFixed')

# Extract table headers
headers = [header.text.strip() for header in table.find_elements(By.CSS_SELECTOR, 'thead th')]

# Extract table rows
rows = []
for tr in table.find_elements(By.CSS_SELECTOR, 'tbody tr'):
    cells = tr.find_elements(By.CSS_SELECTOR, 'td')
    row = [cell.text.strip() for cell in cells]
    rows.append(row)

# Create a DataFrame
df = pd.DataFrame(rows, columns=headers)

# Close the browser
driver.close()

# Display the DataFrame
df.to_csv("output.csv",index=False)