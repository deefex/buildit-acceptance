from pages.locators import Locators
from pages.daily_forecast_row import DailyForecastRow


class DailyForecasts(object):
    """Daily forecasts page element"""

    def __init__(self, driver):
        self.driver = driver

    def row(self, index):
        return DailyForecastRow(self.driver, self.all_rows[index])

    def row_count(self):
        return len(self.driver.find_elements(*Locators.DAILY_FORECAST_ROW))

    @property
    def table(self):
        return self.driver.find_element(*Locators.DAILY_FORECAST_TABLE)

    @property
    def all_rows(self):
        return self.table.find_elements(*Locators.DAILY_FORECAST_ROW)