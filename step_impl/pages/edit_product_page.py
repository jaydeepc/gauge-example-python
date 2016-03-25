from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class EditProductPageLocators:
    update_button = (By.NAME, "commit")
    author = (By.ID, 'product_author')
    description = (By.ID, 'product_description')
    title = (By.ID, 'product_title')


class EditProductPage(BasePage):
    url = '{url}products/{{id}}/edit'.format(url=BasePage.admin_url)

    def set_attribute_value(self, specifier, value):
        self.set(getattr(EditProductPageLocators, specifier), value)

    def save(self):
        self.click(EditProductPageLocators.update_button)

    def visit(self):
        self.driver.get(self.url.format(id=DataStoreFactory.scenario_data_store().get("product_id")))
