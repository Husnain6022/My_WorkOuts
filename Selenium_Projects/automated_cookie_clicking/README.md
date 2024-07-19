# Cookie Clicker Automation Bot

This project automates the gameplay for the Cookie Clicker game using Selenium WebDriver. The bot clicks the cookie and purchases upgrades to maximize the cookies per second (CPS).

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [Algorithms](#algorithms)
  - [Algorithm 1: Most Expensive Affordable Upgrade](#algorithm-1-most-expensive-affordable-upgrade)
  - [Algorithm 2: Purchase All Affordable Upgrades](#algorithm-2-purchase-all-affordable-upgrades)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- Automated cookie clicking
- Periodic checking and purchasing of upgrades
- Two different algorithms for purchasing upgrades:
  - **Algorithm 1**: Purchases the most expensive affordable upgrade every 5 seconds
  - **Algorithm 2**: Purchases all affordable upgrades every 5 seconds

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/cookie-clicker-automation.git
    cd cookie-clicker-automation
    ```

2. **Install the required packages:**
    ```bash
    pip install selenium
    ```

3. **Download the appropriate WebDriver for your browser:**
    - [ChromeDriver](https://sites.google.com/chromium.org/driver/) for Chrome
    - [GeckoDriver](https://github.com/mozilla/geckodriver/releases) for Firefox

4. **Update the path to the WebDriver in the script if necessary.**

## Usage

1. **Run the script:**
    ```bash
    python cookie_clicker.py
    ```

2. The bot will start clicking the cookie and purchasing upgrades according to the specified algorithm.

## Algorithms

### Algorithm 1: Most Expensive Affordable Upgrade

This algorithm checks the right-hand pane every 5 seconds to see which upgrades are affordable and purchases the most expensive one.

### Algorithm 2: Purchase All Affordable Upgrades

This algorithm checks the right-hand pane every 5 seconds and purchases all affordable upgrades.

### Switching Algorithms

To switch between algorithms, you can modify the logic inside the script to choose your preferred strategy.

## Example Output

After running the bot for 5 minutes, the script will print the "cookies per second" (CPS) to the console. Example output:

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.


## Acknowledgments

This project was developed as part of my portfolio. Special thanks to resources and communities that provide guidance and support for improving code quality.

---

Feel free to reach out with any questions or feedback!
