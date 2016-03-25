from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class CreateProductPageLocators:
    submit = (By.NAME, "commit")
    image = (By.ID, 'product_image_file_name')
    price = (By.ID, 'product_price')
    author = (By.ID, 'product_author')
    description = (By.ID, 'product_description')
    title = (By.ID, 'product_title')


class CreateProductPage(BasePage):
    url = '{}products/new'.format(BasePage.admin_url)

    def create(self, title, desc, author, price):
        self.set(CreateProductPageLocators.title, title)
        self.set(CreateProductPageLocators.description, desc)
        self.set(CreateProductPageLocators.author, author)
        self.set(CreateProductPageLocators.price, price)
        self.set(CreateProductPageLocators.image, "not available")
        self.click(CreateProductPageLocators.submit)

    def visit(self):
        self.driver.get(self.url)
