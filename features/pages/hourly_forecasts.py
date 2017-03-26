from pages.locators import Locators
from pages.hourly_forecast_row import HourlyForecastRow


class HourlyForecasts(object):
    """Hourly forecasts page element"""

    def __init__(self, driver, table):
        self.driver = driver
        self.table = table

    def row(self, index):
        return HourlyForecastRow(self.driver, self.all_rows[index])

    @property
    def all_rows(self):
        return self.table.find_elements(*Locators.HOURLY_FORECAST_ROW)

    def row_count(self):
        return sum(row.is_displayed() for row in self.all_rows)

    def rows(self):
        forecasts = []
        for row in self.all_rows:
            forecasts.append(HourlyForecastRow(self.driver, row))
        return forecasts