# Amazon Price Tracker
# Overview
This project is a Python-based web scraper that monitors the price of a specific product on Amazon and sends an email notification when the price drops below a specified threshold. The scraper uses BeautifulSoup for HTML parsing and smtplib for sending email alerts.

# Features
Web Scraping: Extracts product title and price from an Amazon product page.
Price Comparison: Compares the current price with a user-defined target price.
Email Alerts: Sends an email notification if the product price is lower than the target price.
Environment Variables: Stores sensitive information like email credentials and target price securely using a .env file.

# Code Explanation
Web Scraping: Uses BeautifulSoup to parse the HTML of the Amazon product page and extract the title and price.
Price Comparison: Compares the extracted price with the target price.
Email Notification: Sends an email if the current price is less than the target price using smtplib.

# Requirements

Python 3.x
BeautifulSoup4
Requests
Python-dotenv