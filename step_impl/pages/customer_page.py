from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class CustomerPage(BasePage):
    url = '{}customers/'.format(BasePage.admin_url)
    user_name = (By.ID, 'q_username')
    submit = (By.NAME, 'commit')
    result = (By.XPATH, '//table/tbody/tr[1]/td[3]')

    def search_user(self, username):
        self.set(self.user_name, username)
        self.click(self.submit)

    def verify_user_listed(self, username):
        assert self.get(self.result) == username

    def visit(self):
        self.driver.get(self.url)
