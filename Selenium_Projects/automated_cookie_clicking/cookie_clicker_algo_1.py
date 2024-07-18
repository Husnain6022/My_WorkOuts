import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the browser driver (example with Chrome)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# Open the game
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get the cookie to click
cookie = driver.find_element(By.ID, 'cookie')

# Get list of each item id's
div_items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute('id') for item in div_items]

# Initial timeouts
timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    # Check for upgrades every second
    if time.time() > timeout:
        # Get item costs
        text = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_costs = []
        for item in text:
            if item.text:
                cost = int(item.text.split('-')[1].strip().replace(',', ''))
                item_costs.append(cost)

        # Create a dictionary of costs and item ids
        cost_id = {item_costs[n]: item_ids[n] for n in range(len(item_costs))}

        # Get current cookie count
        current_count = driver.find_element(By.ID, 'money').text
        current_count = int(current_count.replace(',', ''))

        # Find affordable upgrades
        affordable_upgrades = {cost: id for cost, id in cost_id.items() if current_count >= cost}

        # Purchase the most expensive affordable upgrade
        if affordable_upgrades:
            max_upgrade_cost = max(affordable_upgrades)
            driver.find_element(By.ID, affordable_upgrades[max_upgrade_cost]).click()

        # Reset the timeout
        timeout = time.time() + 5

    # Stop the bot after 5 minutes and print cookies per second
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, 'cps').text
        print(f"Cookies per second: {cookie_per_s}")
        break

driver.quit()
