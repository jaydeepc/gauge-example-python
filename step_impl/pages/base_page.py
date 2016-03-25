import os


class BasePage(object):
    URL = os.getenv('APP_ENDPOINT')
    ADMIN_URL = '{}admin/'.format(URL)

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.find_element(*element).click()

    def set(self, element, value):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def get(self, element):
        return self.driver.find_element(*element).text
