from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class EditProductPage(BasePage):
    url = '{url}products/{{id}}/edit'.format(url=BasePage.admin_url)
    title = (By.ID, 'product_title')
    description = (By.ID, 'product_description')
    author = (By.ID, 'product_author')
    update_button = (By.NAME, "commit")

    def set_attribute_value(self, specifier, value):
        self.set(getattr(self, specifier), value)

    def save(self):
        self.click(self.update_button)

    def visit(self):
        self.driver.get(self.url.format(id=DataStoreFactory.scenario_data_store().get("product_id")))
