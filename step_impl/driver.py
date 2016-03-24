from getgauge.python import after_suite
from selenium import webdriver


@after_suite
def close():
    DriverFactory.driver.close()


class DriverFactory(object):
    driver = webdriver.Firefox()
