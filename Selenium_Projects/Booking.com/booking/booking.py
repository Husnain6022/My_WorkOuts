import os
from selenium import webdriver
import booking.constants as const
from selenium.webdriver.common.by import By


class Booking(webdriver.Chrome):

    def __init__(self, driver_path=const.PATH, teardown=False):
        os.environ['PATH'] += driver_path
        self.teardown = teardown
        choose_options = webdriver.ChromeOptions()
        choose_options.add_experimental_option("detach", True)
        super(Booking, self).__init__(options=choose_options)
        self.maximize_window()
        self.implicitly_wait(15)



    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def first_page(self):
        self.get(const.URL)

    def change_currency(self):
        pass

    def destination(self, value):
        try:
            dismiss = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Dismiss sign-in info."]')
            dismiss.click()
        except Exception as e:
            print(f'Here is the error {e}.')


    
        destination_input = self.find_element(By.CSS_SELECTOR, 'input[name="ss"]')
        destination_input.clear()
        destination_input.send_keys(value)

        first_location = self.find_element(By.CSS_SELECTOR, 'li[id="autocomplete-result-0"]')
        first_location.click()


    def check_in_dates(self,check_in_date, check_out_date):
        check_in_date = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_in_date}"]')
        check_out_date = self.find_element(By.CSS_SELECTOR, f'span[data-date="{check_out_date}"]')

        check_in_date.click()
        check_out_date.click()

    def select_adults(self, count=1):
        select_box = self.find_element(By.CSS_SELECTOR, 'button[data-testid="occupancy-config"]')
        select_box.click()

        while True:
            adult_decrease = self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[1]')
            adult_decrease.click()

            group_adults = self.find_element(By.ID, "group_adults")
            number_of_adults = group_adults.get_attribute('value')
            if int(number_of_adults) == 1:
                break

        adult_increase = self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/form/div[1]/div[3]/div/div/div/div/div[1]/div[2]/button[2]')

        for _ in range(count - 1):
            adult_increase.click()
