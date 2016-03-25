import datetime
import time

from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class SignUpPageLocators:
    SUBMIT = (By.NAME, 'commit')
    CONFIRM_PASSWORD = (By.ID, 'user_password_confirmation')
    PASSWORD = (By.ID, 'user_password')
    EMAIL = (By.ID, 'user_email')
    USER_NAME = (By.ID, 'user_username')


class SignUpPage(BasePage):
    URL = '{}signup/'.format(BasePage.URL)

    def signup(self):
        user_name = 'user_{}'.format(time.mktime(datetime.datetime.now().timetuple()))
        self.set(SignUpPageLocators.USER_NAME, user_name)
        self.set(SignUpPageLocators.EMAIL, '{}@gmail.com'.format(user_name))
        self.set(SignUpPageLocators.PASSWORD, 'password')
        self.set(SignUpPageLocators.CONFIRM_PASSWORD, 'password')
        self.click(SignUpPageLocators.SUBMIT)
        DataStoreFactory.scenario_data_store().put('current_user', user_name)

    def visit(self):
        self.driver.get(self.URL)
