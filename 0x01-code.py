# Import necessary modules
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Read Excel file into a pandas DataFrame
data = pd.read_excel("path/to/excel_filename.xlsx")

# Set up options for Firefox browser using Options class
options = Options()
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--lang=en-US")

# Create Firefox browser instance with specified options
driver = webdriver.Firefox(
    options=options,
    executable_path="C:/bin/geckodriver",
    firefox_binary=FirefoxBinary(),
    keep_alive=True,
)

# Navigate to the Google Form URL
driver.get("GOOGLE_FORM_URL")

# Loop through each row in the DataFrame
for row in data.itertuples():

    # Wait for page to load
    driver.implicitly_wait(30)

    # Find all input elements on the page using a CSS selector
    input_elements = driver.find_elements(By.CSS_SELECTOR, "input.CSS_SELECTOR")

    # Iterate over input elements and enter data from Excel file
    for i, element in enumerate(input_elements):
        element.send_keys(str(row[i + 1]))

    # Find the submit button on the page using an XPath expression
    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")

    # Click the submit button to submit the form
    submit_button.click()

    # Wait for page to load
    driver.implicitly_wait(30)

    # Navigate back to the Google Form URL
    driver.get("GOOGLE_FORM_URL")

# Close the browser and end the Selenium session
driver.quit()
