import datetime
import time

from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class SignUpPage(BasePage):
    url = '{}signup/'.format(BasePage.url)
    user_name = (By.ID, 'user_username')
    email = (By.ID, 'user_email')
    password = (By.ID, 'user_password')
    confirm_password = (By.ID, 'user_password_confirmation')
    submit = (By.NAME, "commit")

    def signup(self):
        user_name = 'user_{}'.format(time.mktime(datetime.datetime.now().timetuple()))
        self.set(self.user_name, user_name)
        self.set(self.email, '{}@gmail.com'.format(user_name))
        self.set(self.password, 'password')
        self.set(self.confirm_password, 'password')
        self.click(self.submit)
        DataStoreFactory.scenario_data_store().put('current_user', user_name)

    def visit(self):
        self.driver.get(self.url)
