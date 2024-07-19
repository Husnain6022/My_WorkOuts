import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

load_dotenv()

chose_option = webdriver.ChromeOptions()
chose_option.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chose_option)


driver.get('https://x.com/home')


CROSS_BUTTON = os.environ['CROSS_BUTTON']
REJECT_COOKIES = os.environ['REJECT_COOKIES']
SIGN_IN = os.environ['SIGN_IN']
EMAIL_INPUT = os.environ['EMAIL_INPUT']
EMAIL = os.environ["EMAIL"]
NEXT_BUTTON = os.environ['NEXT_BUTTON']
PASSWORD_INPUT = os.environ['PASSWORD_INPUT']
PASSWORD = os.environ['PASSWORD']

cross_button = driver.find_element(By.CSS_SELECTOR, CROSS_BUTTON)
cross_button.click()

reject_cookies = driver.find_element(By.CSS_SELECTOR, REJECT_COOKIES)
reject_cookies.click()

sign_in = driver.find_element(By.XPATH, SIGN_IN)
sign_in.click()

time.sleep(15)
input_keys = driver.find_element(By.NAME, EMAIL_INPUT)
input_keys.send_keys(EMAIL)

next_button = driver.find_element(By.XPATH, NEXT_BUTTON)
next_button.click()
time.sleep(2)
password_input = driver.find_element(By.NAME, PASSWORD_INPUT)
password_input.send_keys(PASSWORD, Keys.ENTER)

