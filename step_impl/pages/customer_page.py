from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class CustomerPageLocators:
    RESULT = (By.XPATH, '//table/tbody/tr[1]/td[3]')
    SUBMIT = (By.NAME, 'commit')
    USER_NAME = (By.ID, 'q_username')


class CustomerPage(BasePage):
    URL = '{}customers/'.format(BasePage.ADMIN_URL)

    def search_user(self, username):
        self.set(CustomerPageLocators.USER_NAME, username)
        self.click(CustomerPageLocators.SUBMIT)

    def verify_user_listed(self, username):
        assert self.get(CustomerPageLocators.RESULT) == username

    def visit(self):
        self.driver.get(self.URL)
