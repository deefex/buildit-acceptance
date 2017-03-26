import time

from behave import given, when, then

from pages.weather_forecast import ForecastPage


@given(u'the user navigates to the forecast page')
def step_impl(context):
    context.forecast_page = ForecastPage(context.browser)


@given(u'{city_name} is entered into the city field')
def step_impl(context, city_name):
    context.forecast_page.set_city_name(city_name)


@given(u'day one\'s hourly forecast is visible')
def step_impl(context):
    context.forecast_page.daily_forecasts.row(0).click()


@when(u'they select one of the daily forecasts')
def step_impl(context):
    context.forecast_page.daily_forecasts.row(0).click()


@when(u'they select the same daily forecast')
def step_impl(context):
    context.forecast_page.daily_forecasts.row(0).click()
    time.sleep(2)


@then(u'the forecast page is available')
def step_impl(context):
    assert context.forecast_page.is_loaded(), "The forecast page has not been loaded as expected"


@then(u'an error message is visible')
def step_impl(context):
    assert context.forecast_page.error_is_visible(), "The error message is not visible as expected"


@then(u'Glasgow is the default city')
def step_impl(context):
    city_name = context.forecast_page.get_city_name()
    assert city_name == 'Glasgow', "City name is %s. Expected Glasgow" % city_name


@then(u'a five day forecast is visible')
def step_impl(context):
    rows = context.forecast_page.daily_forecasts.row_count()
    assert rows == 5, "%s day forecast displayed. Expected 5 " % rows


@then(u'the hourly forecast will be revealed')
def step_impl(context):
    rows = context.forecast_page.daily_forecasts.row(0).hourly_forecasts.row_count()
    assert rows > 0, "%s hourly forecast rows displayed. Expected > 0" % rows


@then(u'the hourly forecast will be hidden')
def step_impl(context):
    rows = context.forecast_page.daily_forecasts.row(0).hourly_forecasts.row_count()
    assert rows == 0, "%s hourly forecast rows displayed. Expected 0" % rows


@then(u'the daily forecast summary shows the most current hourly condition')
def step_impl(context):
    daily = context.forecast_page.daily_forecasts.row(0).condition
    hourly = context.forecast_page.daily_forecasts.row(0).hourly_forecasts.row(0).condition
    assert daily == hourly, "Daily condition summary is %s, expected %s" % (daily, hourly)


@then(u'the daily forecast summary shows the most current hourly wind speed')
def step_impl(context):
    daily = context.forecast_page.daily_forecasts.row(0).wind_speed
    hourly = context.forecast_page.daily_forecasts.row(0).hourly_forecasts.row(0).wind_speed
    assert daily == hourly, "Daily wind speed summary is %s, expected %s" % (daily, hourly)


@then(u'the daily forecast summary shows the most current hourly wind direction')
def step_impl(context):
    daily = context.forecast_page.daily_forecasts.row(0).wind_direction
    hourly = context.forecast_page.daily_forecasts.row(0).hourly_forecasts.row(0).wind_direction
    assert daily == hourly, "Daily wind speed summary is %s, expected %s" % (daily, hourly)


@then(u'the daily forecast summary shows the aggregate rainfall')
def step_impl(context):
    summary_daily_rainfall = int(context.forecast_page.daily_forecasts.row(0).rainfall)
    aggregate_hourly_rainfall = context.forecast_page.daily_forecasts.row(0).aggregate_rainfall()
    assert aggregate_hourly_rainfall == summary_daily_rainfall, "Aggregate rainfall is %s, expected %s" % (aggregate_hourly_rainfall, summary_daily_rainfall)


@then(u'the daily forecast should show the maximum hourly temperature')
def step_impl(context):
    daily_max_temperature = int(context.forecast_page.daily_forecasts.row(0).maximum_temperature)
    hourly_max_temperature = context.forecast_page.daily_forecasts.row(0).highest_hourly_temperature()
    assert hourly_max_temperature == daily_max_temperature, "Highest hourly temperature is %s, expected %s" % (hourly_max_temperature, daily_max_temperature)


@then(u'the daily forecast should show the minimum hourly temperature')
def step_impl(context):
    daily_min_temperature = int(context.forecast_page.daily_forecasts.row(0).minimum_temperature)
    hourly_min_temperature = context.forecast_page.daily_forecasts.row(0).lowest_hourly_temperature()
    assert hourly_min_temperature == daily_min_temperature, "Lowest hourly temperature is %s, expected %s" % (hourly_min_temperature, daily_min_temperature)



