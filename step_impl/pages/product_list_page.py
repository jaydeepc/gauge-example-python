from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class ProductListPage(BasePage):
    url = '{}products/'.format(BasePage.admin_url)
    title = (By.ID, 'q_title')
    submit = (By.NAME, "commit")
    first_product = (By.XPATH, '//table/tbody/tr[1]/td[1]/a')

    def search(self, name):
        self.set(self.title, name)
        self.click(self.submit)

    def open_first_product(self):
        self.driver.find_element(*self.first_product).click()

    def visit(self):
        self.driver.get(self.url)
