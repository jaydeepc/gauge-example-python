from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class ProductListPageLocators:
    first_product = (By.XPATH, '//table/tbody/tr[1]/td[1]/a')
    submit = (By.NAME, "commit")
    title = (By.ID, 'q_title')


class ProductListPage(BasePage):
    url = '{}products/'.format(BasePage.admin_url)

    def search(self, name):
        self.set(ProductListPageLocators.title, name)
        self.click(ProductListPageLocators.submit)

    def open_first_product(self):
        self.click(ProductListPageLocators.first_product)

    def visit(self):
        self.driver.get(self.url)
