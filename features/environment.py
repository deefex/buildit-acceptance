import os

from selenium import webdriver

APPLICATION_URL = 'http://localhost:3000/'


def before_feature(context, feature):
    cwd = os.getcwd()
    driver_path = os.path.join(cwd, 'features', 'bin')
    os.environ["PATH"] = driver_path


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.browser.get(APPLICATION_URL)


def after_scenario(context, scenario):
    context.browser.quit()

