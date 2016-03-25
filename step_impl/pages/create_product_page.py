from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class CreateProductPageLocators:
    SUBMIT = (By.NAME, 'commit')
    IMAGE = (By.ID, 'product_image_file_name')
    PRICE = (By.ID, 'product_price')
    AUTHOR = (By.ID, 'product_author')
    DESCRIPTION = (By.ID, 'product_description')
    TITLE = (By.ID, 'product_title')


class CreateProductPage(BasePage):
    URL = '{}products/new'.format(BasePage.ADMIN_URL)

    def create(self, title, desc, author, price):
        self.set(CreateProductPageLocators.TITLE, title)
        self.set(CreateProductPageLocators.DESCRIPTION, desc)
        self.set(CreateProductPageLocators.AUTHOR, author)
        self.set(CreateProductPageLocators.PRICE, price)
        self.set(CreateProductPageLocators.IMAGE, 'not available')
        self.click(CreateProductPageLocators.SUBMIT)

    def visit(self):
        self.driver.get(self.URL)
