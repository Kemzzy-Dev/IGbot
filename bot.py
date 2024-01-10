import time
import imaplib
import email
import re
from imapclient import IMAPClient
from email.header import decode_header
from bs4 import BeautifulSoup
from seleniumwire import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException, NoAlertPresentException

# Create new options for every driver instance
def get_options():
    options=uc.ChromeOptions()

    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    options.add_argument("--temp-profile")
    options.add_argument(f'--proxy-server=https://{proxy_parts[2]}:{proxy_parts[3]}@{proxy_parts[0]}:{proxy_parts[1]}')
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_experimental_option("prefs", {
    
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 0,
        "profile.default_content_setting_values.notifications": 1
    })
    return options

def getDriver():
    # Create a new instance of the Chrome driver
    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=service,options=get_options())
    driver.implicitly_wait(10)
    actions = ActionChains(driver)

    return driver, actions

# Setting up proxy
proxy_string = "texas1.thesocialproxy.com:10000:wxk9s2mezahrfqby:lgpn0dzbexqmysrw"
proxy_parts = proxy_string.split(':')

# logging
logger = logging.getLogger('selenium')
logger.setLevel(logging.INFO)


class IGBot():
    def __init__(self, username, password, newUsername, newEmail, newEmailPassword) -> None:
        self.username = username
        self.password = password
        self.newEmail = newEmail
        self.newUsername = newUsername
        self.newEmailPassword = newEmailPassword

        # Keep track of the session attempts
        self.attempts = 1

    def loginIG(self, driver):
        
        # Instagram page
        driver.get('https://instagram.com/accounts/login/')

        # check if the login attempt is the first or second time so that we can choose between the normal username or new username
        if self.attempts == 1:
            # Wait for the username input field to be present and input username
            username_input = WebDriverWait(driver,  10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            username_input.send_keys(self.username)
            self.attempts += 1

        elif self.attempts == 2:
            # Wait for the username input field to be present and input username
            username_input = WebDriverWait(driver,  10).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            username_input.send_keys(self.newUsername)
            self.attempts -= 1

        # Locate the password input field and enter the password
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)
        

    def changeEmail(self):
        # Open a new window
        # driver.execute_script("window.open('', '_blank');")
        driver, actions = getDriver()
        self.loginIG(driver)

        try:
            # Check if the error message is displayed
            error_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Sorry, your password was incorrect. Please double-check your password.')]")
            if error_element.is_displayed():
                print("Username or password incorrect")
                exit()

        except NoSuchElementException:
            # driver.get("https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point")

            # wait until page loading completes and then go to the email accounts settings
            try:
                WebDriverWait(driver, 50).until(
                    EC.url_contains("onetap")
                )
                driver.get("https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point")
            except:
                print("Time Up")
            
            driver.get("https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point")

            # Input a new email address
            newEmailForm = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.TAG_NAME, 'input'))
            )
            newEmailForm.send_keys(self.newEmail)

            # Click on the checkbox to accept the terms, tab to the done button
            checkButton = driver.find_element(By.NAME, 'noform')
            checkButton.click()
            checkButton.send_keys(Keys.TAB)

            # Click on the Done button to submit information
            time.sleep(3)
            actions.send_keys(Keys.RETURN)
            actions.perform()

            #Get the OTP from the mail and input in the field
            try:
                otp = getOTP(self.newEmail, self.newEmailPassword)
            except Exception as e:
                print("Error, try again.")
                print(e)
                exit()

            # Select field
            otpForm = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.ID, ':rd:'))
            )

            # Enter otp and click next
            otpForm.send_keys(otp)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.TAB)
            time.sleep(3)
            actions.send_keys(Keys.ENTER)

            time.sleep(3)

            # Refresh to ensure the name propagates around instagram
            refresh_count = 3

            for _ in range(refresh_count):
                # Refresh the page
                driver.refresh()

                # Optional: Add a delay between each refresh
                time.sleep(2)

            driver.quit()


    def changeName(self) -> None:  
        driver, actions = getDriver()
        
        # Login the email
        self.loginIG(driver) 

        try:
            # Check if the error message is displayed
            error_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Sorry, your password was incorrect. Please double-check your password.')]")
            if error_element.is_displayed():
                print("Username or password incorrect")
                exit()

        except NoSuchElementException:
            try:
                WebDriverWait(driver, 50).until(
                    EC.url_contains("onetap")
                )
                # Load the link for settings
                driver.get("https://accountscenter.instagram.com/profiles")
            except:
                print("Time Up, Network Error")
                exit()

            #Get the user link and load the page
            Userlink = driver.find_elements(By.XPATH, "//*[@role='link']")[10].get_attribute("href")
            driver.get(f"{Userlink}username/manage/")

            # Click on the username settings and replace it with the new username
            newUsernameInput = WebDriverWait(driver, 50).until(
                EC.presence_of_element_located((By.TAG_NAME, 'input'))
            )
            newUsernameInput.send_keys(Keys.CONTROL + "a")
            newUsernameInput.send_keys(Keys.DELETE)
            newUsernameInput.send_keys(self.newUsername)

            # Moves the cursor to the Done button and clicks 
            time.sleep(3)
            newUsernameInput.click()
            actions.send_keys(Keys.TAB)
            actions.send_keys(Keys.TAB)
            time.sleep(3)
            actions.send_keys(Keys.ENTER)
            actions.perform()

            time.sleep(3)

            # Refresh to ensure the name propagates around instagram
            refresh_count = 3

            for _ in range(refresh_count):
                # Refresh the page
                driver.refresh()

                # Optional: Add a delay between each refresh
                time.sleep(2) 

        driver.quit()
        del driver
        

def getOTP(userEmail:str, password:str) -> str:

    # Outlook IMAP settings
    outlook_server = "outlook.office365.com"

    # Connect to Outlook's IMAP server
    mail = imaplib.IMAP4_SSL(outlook_server)
    mail.login(userEmail, password)

    # Select the mailbox you want to access
    mail.select("inbox")

    # Search for all emails in the inbox
    status, messages = mail.search(None, "ALL")
    messages = messages[0].split()

    # Get the latest email
    latest_email_id = messages[-1]

    # Fetch the email by ID
    status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
    raw_email = msg_data[0][1]

    # Parse the raw email
    msg = email.message_from_bytes(raw_email)

    # Extract the HTML part of the email
    for part in msg.walk():
        content_type = part.get_content_type()

        # Check for text/html parts
        if "text/html" in content_type:
            # Get the HTML content
            html_content = part.get_payload(decode=True).decode("utf-8")

    # Parse the HTML part with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the confirmation code element by its style attribute
    confirmation_code_element = soup.find('td', style='padding:10px;color:#565a5c;font-size:32px;font-weight:500;text-align:center;padding-bottom:25px;')

    # Extract the confirmation code
    if confirmation_code_element:
        confirmation_code = confirmation_code_element.get_text(strip=True)
        code = confirmation_code
    else:
        code = "Confirmation code element not found."
    
    # Close the connection
    mail.logout()

    #return the code
    return code



if __name__ == "__main__":
    try:
        newBot = IGBot('Luisosmani46125', 'mohammad2225','Luisosmani730275', "Jessicaclive049557@hotmail.com", 'XtpBiGae37')

        newBot.changeName()
        time.sleep(5)
        newBot.changeEmail()

        print("Done")
    except WebDriverException as e:
            if "net::ERR_NAME_NOT_RESOLVED" in str(e):
                print("No internet or site not rechable. Try again")
            else:
                print(e)

            