Feature: Build-it Acceptance Tests

  @smoke
  Scenario: The weather page is available
    Given the user navigates to the forecast page
    Then the forecast page is available

  @smoke
  Scenario: The default city is Glasgow
    Given the user navigates to the forecast page
    Then Glasgow is the default city

  @smoke
  Scenario: An error is displayed for an unrecognised city
    Given the user navigates to the forecast page
    And myhometown is entered into the city field
    Then an error message is visible

  @daily
  Scenario Outline: A five day forecast is displayed for a valid city
    Given the user navigates to the forecast page
    And <city_name> is entered into the city field
    Then a five day forecast is visible

  Examples:
    | city_name |
    | aberdeen  |
    | dundee    |
    | edinburgh |
    | glasgow   |
    | perth     |
    | stirling  |

  @hourly
  Scenario: Selecting a day, displays the hourly forecast
    Given the user navigates to the forecast page
    When they select one of the daily forecasts
    Then the hourly forecast will be revealed

  @hourly
  Scenario: De-selecting a day, hides the hourly forecast
    Given the user navigates to the forecast page
    And day one's hourly forecast is visible
    When they select the same daily forecast
    Then the hourly forecast will be hidden

  @daily @summary
  Scenario: Daily forecast summary - condition
    Given the user navigates to the forecast page
    And day one's hourly forecast is visible
    Then the daily forecast summary shows the most current hourly condition

  @daily @summary
  Scenario: Daily forecast summary - wind speed and direction
    Given the user navigates to the forecast page
    And day one's hourly forecast is visible
    Then the daily forecast summary shows the most current hourly wind speed
    And the daily forecast summary shows the most current hourly wind direction

  @daily @summary
  Scenario: Daily forecast summary - aggregate rainfall
    Given the user navigates to the forecast page
    And day one's hourly forecast is visible
    Then the daily forecast summary shows the aggregate rainfall

  @daily @summary
  Scenario: Daily forecast summary - maximum/minimum temperature
    Given the user navigates to the forecast page
    And day one's hourly forecast is visible
    Then the daily forecast should show the maximum hourly temperature
    And the daily forecast should show the minimum hourly temperature

#  Scenario: All values should be rounded down
#     TODO - Ran out of time :-(