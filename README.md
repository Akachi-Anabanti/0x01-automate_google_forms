# Google Form Automation with Python and Selenium

## Brief description

This repository contains a Python script for automating the process of filling out a Google Form using data from an Excel file. The script uses the [Selenium](https://www.selenium.dev/) library to automate the web browser and the pandas library to read the Excel file.

## Requirements

To use this script, you'll need to have the following installed on your computer

- [x] Python 3.x
- [x] Selenium
- [x] pandas
- [x] openpyxl
- [x] Firefox web browser
- [x] geckodriver

To install firefox, visit the [official Firefox website](https://www.mozilla.org/en-US/firefox/new/) and download the latest version for your operating system

To install geckodriver, visit the [official geckodriver release page](https://github.com/mozilla/geckodriver/releases) and download the latest version for your operating system. Make sure to add the directory containing the geckodriver executable to your PATH environment variable

## Usage

To use the script, follow these steps:

1. Clone the repository to your local machine

   - `git clone https://github.com/Akachi-Anabanti/0x01-automate_google_form.git`

2. Install the required libraries and software
   - `pip3 install selenium`
   - `pip3 install pandas`
   - `pip3 install openpyxl`
3. Replace the `GOOGLE_FORM_URL` placeholder with the URL of your Google form
4. Replace `path/to/excel_filename.xlsx` placeholder in the script with the path to your Excel file
5. Replace the `input.CSS_SELECTOR` with the appropriate selector for your google form. see instruction [below](#how-to-get-css-selector-from-google-forms)

6. Run the Script using the following command
   - `python 0x01-code.py`

The script will automate the process of filling out the Google Form using the data from your Excel file.

## Contributing

If you find a bug or would like to suggest an improvement, please open an issue or submit a pull request.

### How to get css selector from google forms

1. Open the Google input form in your web browser.

2. Right-click on the input field that you want to extract the CSS selector for and select "Inspect" or "Inspect element" from the context menu.
   This will open the browser's developer tools.
3. In the developer tools, locate the HTML code that corresponds to the input field. The code will be highlighted in the Elements tab of
   the developer tools.
4. Right-click on the highlighted code and select "Copy" from the context menu.

5. Select "Copy selector" from the submenu. This will copy the CSS selector for the input field to your clipboard.
