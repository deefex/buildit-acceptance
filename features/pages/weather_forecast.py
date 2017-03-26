import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

from pages.locators import Locators
from pages.daily_forecasts import DailyForecasts


class ForecastPage(object):
    """The forecast page class for the application - there's only one page!"""

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, 'city')))
            return True
        except TimeoutException:
            return False

    def error_is_visible(self):
        return self.driver.find_element(*Locators.ERROR_MESSAGE).is_displayed()

    def set_city_name(self, city_name):
        self.driver.find_element(*Locators.CITY_FIELD).clear()
        self.driver.find_element(*Locators.CITY_FIELD).send_keys(city_name + Keys.ENTER)
        time.sleep(2)

    def get_city_name(self):
        return self.driver.find_element(*Locators.CITY_FIELD).get_attribute('value')

    @property
    def daily_forecasts(self):
        return DailyForecasts(self.driver)

