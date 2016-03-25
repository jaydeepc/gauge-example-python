from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class ProductListPageLocators:
    FIRST_PRODUCT = (By.XPATH, '//table/tbody/tr[1]/td[1]/a')
    SUBMIT = (By.NAME, 'commit')
    TITLE = (By.ID, 'q_title')


class ProductListPage(BasePage):
    URL = '{}products/'.format(BasePage.ADMIN_URL)

    def search(self, name):
        self.set(ProductListPageLocators.TITLE, name)
        self.click(ProductListPageLocators.SUBMIT)

    def open_first_product(self):
        self.click(ProductListPageLocators.FIRST_PRODUCT)

    def visit(self):
        self.driver.get(self.URL)
