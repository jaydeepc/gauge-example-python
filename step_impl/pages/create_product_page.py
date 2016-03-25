from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class CreateProductPage(BasePage):
    url = '{}products/new'.format(BasePage.admin_url)
    title = (By.ID, 'product_title')
    description = (By.ID, 'product_description')
    author = (By.ID, 'product_author')
    price = (By.ID, 'product_price')
    image = (By.ID, 'product_image_file_name')
    submit = (By.NAME, "commit")

    def create(self, title, desc, author, price):
        self.set(self.title, title)
        self.set(self.description, desc)
        self.set(self.author, author)
        self.set(self.price, price)
        self.set(self.image, "not available")
        self.click(self.submit)

    def visit(self):
        self.driver.get(self.url)
