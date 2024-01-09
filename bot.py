import time
import imaplib
import email
import re
from email.header import decode_header
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--temp-profile")

service = Service(executable_path='./chromedriver')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service,options=chrome_options)
driver.implicitly_wait(10)

actions = ActionChains(driver)


class IG:
    def __init__(self) -> None:
        self.username = 'Vullnetzane42145'
        self.password = 'mohammad2225'
        self.newEmail = "Abigailgarcia065337@hotmail.com"
        self.newUsername = 'Vullnetzane64125'

    def loginIG(self):
        # Instagram page
        driver.get('https://instagram.com/accounts/login/')

        # Wait for the username input field to be present and input username
        username_input = WebDriverWait(driver,  10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys(self.username)

        # Locate the password input field and enter the password
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)


    def changeEmail(self):
        # Login to the account
        self.loginIG()

        # wait until page loading completes and then go to the email accounts settings
        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("onetap")
            )
            driver.get("https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point")
        except:
            print("Time Up")

        # Input a new email address
        newEmailForm = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'input'))
        )
        newEmailForm.send_keys(self.newEmail)

        # Click on the checkbox to accept the terms, tab to the done button
        checkButton = driver.find_element(By.NAME, 'noform')
        checkButton.click()
        checkButton.send_keys(Keys.TAB)

        # Click on the Done button to submit information
        actions.send_keys(Keys.RETURN)
        actions.perform()

    def changeName(self):  
        # Login the email
        self.loginIG() 

        try:
            WebDriverWait(driver, 20).until(
                EC.url_contains("onetap")
            )
            # Load the link for settings
            driver.get("https://accountscenter.instagram.com/profiles")
        except:
            print("Time Up")

        #Get the user link and load the page
        Userlink = driver.find_elements(By.XPATH, "//*[@role='link']")[10].get_attribute("href")
        driver.get(f"{Userlink}username/manage/")

        # Click on the username settings and replace it with the new username
        newUsernameInput = WebDriverWait(driver, 20).until(
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
        actions.send_keys(Keys.ENTER)
        actions.perform()
        

def getOTP(self):

    # Outlook IMAP settings
    outlook_server = "outlook.office365.com"
    username = "Abigailgarcia065337@hotmail.com"
    password = "lzOfripy54"

    # Connect to Outlook's IMAP server
    mail = imaplib.IMAP4_SSL(outlook_server)
    mail.login(username, password)

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
    # igLogin = IG()
    emailLogin = Email()

    # igLogin.changeEmail()
    emailLogin.getOTP()
    # time.sleep(10)
    # emailLogin.getOTP()
