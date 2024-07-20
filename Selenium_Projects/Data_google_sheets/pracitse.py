import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# URLs from environment variables
SHEET_LINK = os.environ['SHEET_LINK']
SITE_LINK = os.environ['SITE_LINK']

# Fetch the webpage content
response = requests.get(SITE_LINK)
soup = BeautifulSoup(response.text, "html.parser")

# Extract property details
li_element_a = soup.select(selector="li.ListItem-c11n-8-84-3-StyledListCardWrapper a")
links = [item.get("href") for item in li_element_a]

li_element_addr = soup.select(selector="li.ListItem-c11n-8-84-3-StyledListCardWrapper a address")
addresses = [item.get_text().strip().replace('|', '').replace('#', '') for item in li_element_addr]

div_price_element = soup.select(selector="div.PropertyCardWrapper span")
prices = [item.get_text().split("+")[0].replace('/mo', '') for item in div_price_element]

# Selenium setup for Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

'''
Ensure you have a Google Sheet with three questions set to short answer format:
1. What's the address of the property?
2. What's the price per month?
3. What's the link to the property?

Copy the Google Sheet link and paste it in the SHEET_LINK environment variable.
'''

# Open the Google Sheet
driver.get(SHEET_LINK)
driver.maximize_window()
driver.implicitly_wait(5)

# Wait for user to enter credentials
input('Please enter your credentials in the browser window, then press Enter here: ')

# Iterate through each property and input details into Google Sheet
for i in range(len(addresses)):
    addr_input = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_input = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
    link_input = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    submit_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div")

    # Input property details

    addr_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    #submitting
    
    submit_button.click()

    # to submit another response
    another_response = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
    another_response.click()
