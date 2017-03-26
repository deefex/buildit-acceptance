from pages.locators import Locators


class HourlyForecastRow(object):
    """Hourly forecast table row element"""

    def __init__(self, driver, row):
        self.driver = driver
        self.row = row

    @property
    def hour(self):
        return self.row.find_element(*Locators.HOUR).text

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
        rotation = self.row.find_element(*Locators.WIND_DIRECTION).find_element_by_xpath(".//*[name()='svg']").get_attribute('style')[89:]
        return filter(lambda x: x.isdigit(), rotation)

    @property
    def rainfall(self):
        return self.row.find_element(*Locators.RAINFALL).text.replace("mm", "")

    @property
    def pressure(self):
        return self.row.find_element(*Locators.PRESSURE).text.replace("mb", "")