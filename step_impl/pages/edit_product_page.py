from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class EditProductPageLocators:
    UPDATE_BUTTON = (By.NAME, 'commit')
    AUTHOR = (By.ID, 'product_author')
    DESCRIPTION = (By.ID, 'product_description')
    TITLE = (By.ID, 'product_title')


class EditProductPage(BasePage):
    URL = '{url}products/{{id}}/edit'.format(url=BasePage.ADMIN_URL)

    def set_attribute_value(self, specifier, value):
        self.set(getattr(EditProductPageLocators, specifier.upper()), value)

    def save(self):
        self.click(EditProductPageLocators.UPDATE_BUTTON)

    def visit(self):
        self.driver.get(self.URL.format(id=DataStoreFactory.scenario_data_store().get('product_id')))
