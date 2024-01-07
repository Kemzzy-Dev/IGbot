from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import imaplib
import email
from email.header import decode_header

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--no-sandbox")

service = Service(executable_path='./chromedriver')

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service,options=chrome_options)

class IG:
    def __init__(self) -> None:
        self.username = 'Enrikkodra461253'
        self.password = 'mohammad2225'
        self.newEmail = "Ariannalee341303@hotmail.com"

    def loginIG(self):
        driver.get('https://www.instagram.com/accounts/login/')

        # Wait for the username input field to be present
        username_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username_input.send_keys(self.username)

        # Locate the password input field and enter the password
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys(self.password)

        # Submit the login form
        password_input.send_keys(Keys.RETURN)


    def changeEmail(self):
        self.loginIG()

        time.sleep(5)

        driver.get("https://accountscenter.instagram.com/personal_info/contact_points/?contact_point_type=email&dialog_type=add_contact_point")
        time.sleep(3)

        newEmailForm = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'input'))
        )
        newEmailForm.send_keys(self.newEmail)

        checkButton = driver.find_element(By.NAME, 'noform')
        checkButton.click()

        time.sleep(3)
        nextButton = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Fz"]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[6]/div[3]/div/div/div/div/div/div/div')
        nextButton.click()

    def changePassword(self):  
        pass 



class Email:
    def __init__(self) -> None:
        self.password = "LAj461ciJS"
        self.email = "Enrikkodra461253@outlook.com"

    # def loginEmail(self):
    #     # URL for Gmail login
    #     gmail_url = 'https://login.live.com/'

    #     # Set up Chrome options for headless mode
    #     # chrome_options.add_argument('--headless')  # Run Chrome in headless mode

    #     # Navigate to Gmail login page
    #     driver.get(gmail_url)

    #     # Locate the email input field and enter the email address
    #     email_field = driver.find_element("name", "loginfmt")
    #     email_field.send_keys(self.email)
    #     email_field.send_keys(Keys.RETURN)

    #     # Locate the password input field and enter the password
    #     password_field = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located((By.NAME, 'passwd'))
    #     )
    #     password_field.send_keys(self.password)
    #     password_field.send_keys(Keys.RETURN)

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
    time.sleep(10)
    emailLogin.getOTP()
