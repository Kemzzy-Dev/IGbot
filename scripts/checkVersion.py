import subprocess
import requests
import os
import zipfile
import shutil
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 


def check_and_update_chromedriver():
    chromedriver_path = '../chromedriver'
    try:
        # Launch Chrome using Selenium without specifying ChromeDriver path
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Optional: Run Chrome in headless mode
        driver = webdriver.Chrome(options=options)

        # Get the installed version of Chrome
        chrome_version = driver.capabilities['browserVersion']

        # Close the Selenium WebDriver
        driver.quit()

        # Check if the specified ChromeDriver is present and compatible
        if 'chrome_version' in locals() and 'driver_version' in locals() and chrome_version[0:2] == driver_version[0:2]:
            print(f"Chrome version: {chrome_version}, ChromeDriver version: {driver_version}")
            return True
        else:
            print(f"Chrome version: {chrome_version}, ChromeDriver version: {driver_version}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Determine the URL and file name based on the operating system
    if platform.system() == 'Windows':
        url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_win32.zip"
        filename = 'chromedriver.exe'
    else:
        url = f"https://chromedriver.storage.googleapis.com/{chrome_version}/chromedriver_linux64.zip"
        filename = 'chromedriver'

    # Download the corresponding version of ChromeDriver
    r = requests.get(url)
    z = zipfile.ZipFile(zipfile.BytesIO(r.content))
    z.extractall('.')

    # Rename the extracted file to chromedriver
    shutil.move(filename, chromedriver_path)

    print(f"Downloaded and updated ChromeDriver to version compatible with Chrome {chrome_version}")
    
# Check and update ChromeDriver
