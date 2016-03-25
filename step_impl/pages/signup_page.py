import datetime
import time

from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class SignUpPageLocators:
    submit = (By.NAME, "commit")
    confirm_password = (By.ID, 'user_password_confirmation')
    password = (By.ID, 'user_password')
    email = (By.ID, 'user_email')
    user_name = (By.ID, 'user_username')


class SignUpPage(BasePage):
    url = '{}signup/'.format(BasePage.url)

    def signup(self):
        user_name = 'user_{}'.format(time.mktime(datetime.datetime.now().timetuple()))
        self.set(SignUpPageLocators.user_name, user_name)
        self.set(SignUpPageLocators.email, '{}@gmail.com'.format(user_name))
        self.set(SignUpPageLocators.password, 'password')
        self.set(SignUpPageLocators.confirm_password, 'password')
        self.click(SignUpPageLocators.submit)
        DataStoreFactory.scenario_data_store().put('current_user', user_name)

    def visit(self):
        self.driver.get(self.url)
