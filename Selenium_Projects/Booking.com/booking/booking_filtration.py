from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Booking_Filtration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_start_rating(self, *values):
        star_filtration_box = self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[3]/div[8]")
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR, "*")

        for value in values:
            for star_child_element in star_child_elements:
                print(star_child_element.get_attribute('innerHTML'))
                if str(star_child_element.get_attribute('innerHTML')).strip() == f'{value} star':
                    star_child_element.click()
                else:
                    print('not find')

