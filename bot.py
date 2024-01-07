from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

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
        username_input = WebDriverWait(driver, 10).until(
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

        newEmailForm =  driver.find_element("id", ":rv:")
        newEmailForm.send_keys(self.newEmail)

    def changePassword(self):
        pass 



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
        password_field = driver.find_element("name", "passwd")
        password_field.send_keys(self.password)
        time.sleep(2)

        signInButton = driver.find_element("id", "idSIButton9")
        signInButton.click()

        continueButton = driver.find_element("id", "id__0")
        continueButton.click()

        # Take a screenshot (optional - useful for headless mode)
        driver.save_screenshot('gmail_headless.png')

    def getOTP(self):
        pass


if __name__ == "__main__":
    igLogin = IG()
    igLogin.changeEmail()
