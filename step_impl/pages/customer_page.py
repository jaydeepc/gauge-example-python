from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class CustomerPageLocators:
    result = (By.XPATH, '//table/tbody/tr[1]/td[3]')
    submit = (By.NAME, 'commit')
    user_name = (By.ID, 'q_username')


class CustomerPage(BasePage):
    url = '{}customers/'.format(BasePage.admin_url)

    def search_user(self, username):
        self.set(CustomerPageLocators.user_name, username)
        self.click(CustomerPageLocators.submit)

    def verify_user_listed(self, username):
        assert self.get(CustomerPageLocators.result) == username

    def visit(self):
        self.driver.get(self.url)
