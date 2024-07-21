import os
from selenium import webdriver
from booking import constants as const


class Booking(webdriver.Chrome):

    def __init__(self, driver_path = const.PATH):
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__()
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()

    def first_page(self):
        self.get(const.URL)