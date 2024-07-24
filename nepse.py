from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup
from datetime import timedelta, datetime
import os
import time

# Initialize the WebDriver (assuming you're using Chrome)
driver = webdriver.Chrome()

# Get today's date
current_date = datetime.now()

# Define the number of days to go back
days_to_scrape = 100

try:
    # Loop to go back for the specified number of days
    for _ in range(days_to_scrape):
        try:
            # Open the website
            driver.get("https://www.sharesansar.com/today-share-price")

            # Wait for the date picker to be present
            date_picker = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "fromdate"))
            )

            # Clear any existing value in the input field and input the desired date
            date_picker.clear()
            date_picker.send_keys(current_date.strftime("%Y-%m-%d"))
            date_picker.send_keys(Keys.RETURN)

            # Wait until the search button is clickable
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "btn_todayshareprice_submit"))
            )

            # Click the search button
            search_button.click()

            # Wait for the table to be present in the DOM
            table_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'headFixedWrapper'))
            )

            # Introduce an additional wait to ensure data is fully loaded
            time.sleep(5)  # Adjust sleep time as needed

            # Get the page source and parse it with BeautifulSoup
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            # Locate the target div and table
            target_div = soup.find('div', class_='headFixedWrapper')
            table = target_div.find('table', {'id': 'headFixed'}) if target_div else None

            if table:
                # Extract table headers
                headers = [th.text.strip() for th in table.find('thead').find_all('th')]
                print(f"Headers: {headers}")

                # Extract table rows
                rows = []
                for tr in table.find('tbody').find_all('tr'):
                    cells = tr.find_all('td')
                    if len(cells) == len(headers):  # Ensure row has the correct number of columns
                        row = [cell.text.strip() for cell in cells]
                        rows.append(row)
                    else:
                        print(f"Row with unexpected number of columns: {tr}")

                # Log the rows to diagnose any issues
                print(f"First row: {rows[0] if rows else 'No rows found'}")

                # Create a DataFrame if rows are found
                if rows:
                    df = pd.DataFrame(rows, columns=headers)
                    print(df.head(1))

                    # Ensure the directory exists
                    if not os.path.exists('data'):
                        os.makedirs('data')

                    # Save the DataFrame to a CSV file
                    file_name = f"data/data_{current_date.strftime('%Y-%m-%d')}.csv"
                    df.to_csv(file_name, index=False)
                    print(f"Data saved to {file_name}")
                else:
                    print(f"No valid rows found for date {current_date.strftime('%Y-%m-%d')}")
            else:
                print(f"No table found for date {current_date.strftime('%Y-%m-%d')}")

            # Move to the previous day
            current_date -= timedelta(days=1)

        except Exception as e:
            print(f"An error occurred: {e}")



finally:
    # Close the browser
    driver.quit()
    
a = selenium_web()
for i in a:
    print(i.head())
