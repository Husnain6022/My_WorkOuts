import os
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv

load_dotenv()


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Host": "www.amazon.com",
    "Sec-Ch-Ua": "\"Chromium\";v=\"91\", \"Not;A Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
}

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text,'html.parser')
title = soup.find(id='productTitle').get_text().strip()
clean_title = ' '.join(title.split())
print(clean_title)
price_tag = soup.select_one('div span.aok-offscreen')
price = price_tag.get_text().strip().split('$')[1]
print(price)


target_price = 100
MY_EMAIL = os.environ['MY_EMAIL']
PASSWORD = os.environ['PASSWORD']
LINK = 'https://appbrewery.github.io/instant_pot/'

if float(price) < float(target_price):
    with smtplib.SMTP(os.environ['SMTP_ADDR'], port=587) as connection:
        subject = "Lowest Price Alert"
        body = f"Title: {clean_title}\nPrice: ${price}\n Link to product: {LINK}."
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = MY_EMAIL
        msg['To'] = 'bc150403422@vu.edu.pk'
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs='bc150403422@vu.edu.pk',
                            msg=msg.as_string())


