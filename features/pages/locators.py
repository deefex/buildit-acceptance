from selenium.webdriver.common.by import By


class Locators(object):
    # Page locators
    CITY_FIELD = (By.ID, "city")
    ERROR_MESSAGE = (By.XPATH, "//div[@data-test='error']")

    # Daily forecast locators
    DAILY_FORECAST_TABLE = (By.XPATH, "//div[@id='root']/div")
    DAILY_FORECAST_ROW = (By.XPATH, "//div[@style='padding-bottom: 20px;']")

    # Hourly forecast locators
    HOURLY_FORECAST_TABLE = (By.XPATH, "//div[@class='details']")
    HOURLY_FORECAST_ROW = (By.XPATH, ".//div[@class='detail']")

    # Daily specific detail locators
    DAY = (By.XPATH, ".//span[contains(@data-test,'day')]")
    DATE = (By.XPATH, "//span[contains(@data-test,'date')]")

    # Hourly specific detail locators
    HOUR = (By.CLASS_NAME, "hour")

    # Weather detail locators - for both DAILY and HOURLY
    CELL = (By.CLASS_NAME, "cell")
    CONDITION = (By.CLASS_NAME, "icon")
    MAXIMUM_TEMPERATURE = (By.CLASS_NAME, "max")
    MINIMUM_TEMPERATURE = (By.XPATH, ".//span[contains(@data-test,'minimum')]")
    WIND_SPEED = (By.CLASS_NAME, "speed")
    WIND_DIRECTION = (By.XPATH, ".//span[contains(@data-test, 'direction')]")
    RAINFALL = (By.CLASS_NAME, "rainfall")
    PRESSURE = (By.XPATH, ".//span[contains(@data-test,'pressure')]")

