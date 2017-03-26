from pages.locators import Locators
from pages.hourly_forecasts import HourlyForecasts


class DailyForecastRow(object):
    """Daily forecasts table row element"""

    def __init__(self, driver, row):
        self.driver = driver
        self.row = row

    @property
    def hourly_forecasts(self):
        return HourlyForecasts(self.driver, self.row.find_element(*Locators.HOURLY_FORECAST_TABLE))

    @property
    def day(self):
        return self.row.find_element(*Locators.DAY).text

    @property
    def date(self):
        return self.row.find_element(*Locators.DATE).text

    @property
    def condition(self):
        return self.row.find_element(*Locators.CONDITION).get_attribute('aria-label')

    @property
    def maximum_temperature(self):
        temp = unicode(self.row.find_element(*Locators.MAXIMUM_TEMPERATURE).text)
        return temp.replace(u"\u00B0", "")  # Remove the degrees symbol

    @property
    def minimum_temperature(self):
        temp = unicode(self.row.find_element(*Locators.MINIMUM_TEMPERATURE).text)
        return temp.replace(u"\u00B0", "")  # Remove the degrees symbol

    @property
    def wind_speed(self):
        return self.row.find_element(*Locators.WIND_SPEED).text.replace("kph", "")

    @property
    def wind_direction(self):
        rotation =  self.row.find_element(*Locators.WIND_DIRECTION).find_element_by_xpath(".//*[name()='svg']").get_attribute('style')[89:]
        return filter(lambda x: x.isdigit(), rotation)

    @property
    def rainfall(self):
        return self.row.find_element(*Locators.RAINFALL).text.replace("mm", "")

    @property
    def pressure(self):
        return self.row.find_element(*Locators.PRESSURE).text.replace("mb", "")

    def aggregate_rainfall(self):
        aggregate = 0
        for forecast in self.hourly_forecasts.rows():
            aggregate += int(forecast.rainfall)
        return aggregate

    def highest_hourly_temperature(self):
        temperatures = []
        for forecast in self.hourly_forecasts.rows():
            temperatures.append(int(forecast.maximum_temperature))
        return max(temperatures)

    def lowest_hourly_temperature(self):
        temperatures = []
        for forecast in self.hourly_forecasts.rows():
            temperatures.append(int(forecast.minimum_temperature))
        return min(temperatures)

    def click(self):
        self.row.find_element(*Locators.CELL).click()