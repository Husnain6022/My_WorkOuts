'''   Here is the clean code  '''

import os
from email.mime.text import MIMEText
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

    #Function to fetch and parse details from Amazon

def fetch_product_detail(url, header):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find(id = 'productTitle').get_text().strip()
    clean_title = ' '.join(title.split())
    price = soup.select_one('div span.aok-offscreen').get_text().strip().split('$')[1]
    return clean_title, price

    #Function to send Email_Notification

def send_email(subject, body, from_addr, to_addr, smtp_addr, password):
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    with smtplib.SMTP(smtp_addr, port=587) as connection:
        connection.starttls()
        connection.login(user=from_addr, password=password)
        connection.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())

def main():
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
    target_price = 100
    try:
        title, price = fetch_product_detail(url, headers)
        if float(price) < float(target_price):
            subject = 'Lowest Price Alert'
            body = f'Title: {title} \n Price: ${price} \n link: {url}'
            MY_EMAIL = os.environ['MY_EMAIL']
            PASSWORD = os.environ['PASSWORD']
            TO_ADDR = 'destination_email' #PUT YOUR OWN DESTINATION EMAIL
            SMTP_ADDR = os.environ['SMTP_ADDR']

            send_email(subject,body,MY_EMAIL,TO_ADDR,SMTP_ADDR,PASSWORD)

            print(f'Email sent to: {TO_ADDR}')
        else:
            print(f'The Current Price ${price} is not less then the target price ${target_price}.')

    except Exception as e:
        print(f'as error occurred {e}')

if __name__ == "__main__" :
    main()
