import time
import imaplib
import email
from email.header import decode_header
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
        


class Email:
    def __init__(self) -> None:
        self.password = "LAj461ciJS"
        self.email = "Enrikkodra461253@outlook.com"

    def loginEmail(self):
        # URL for Gmail login
        gmail_url = 'https://login.live.com/'

        # Set up Chrome options for headless mode
        # chrome_options.add_argument('--headless')  # Run Chrome in headless mode

        # Navigate to Gmail login page
        driver.get(gmail_url)

        # Locate the email input field and enter the email address
        email_field = driver.find_element("name", "loginfmt")
        email_field.send_keys(self.email)
        email_field.send_keys(Keys.RETURN)

        # Locate the password input field and enter the password
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'passwd'))
        )
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)

    def getOTP(self):
        # self.loginEmail()

        # driver.get("https://outlook.live.com/mail/0/")

        # Outlook IMAP settings
        outlook_server = "outlook.office365.com"
        username = "Enrikkodra461253@outlook.com"
        password = "LAj461ciJS"

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
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        # Print the subject and the body of the email
        print("Subject:", subject)

        # Extract OTP from the email body (assuming it's in the body)
        otp = "123456"  # Replace with your OTP extraction logic

        # Close the connection
        mail.logout()





if __name__ == "__main__":
    igLogin = IG()
    emailLogin = Email()

    igLogin.changeEmail()
    # time.sleep(10)
    # emailLogin.getOTP()
