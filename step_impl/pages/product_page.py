from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class ProductPageLocators:
    delete_product = (By.LINK_TEXT, 'Delete Product')
    price = (By.XPATH, '//table/tbody/tr[5]/td')
    author = (By.XPATH, '//table/tbody/tr[4]/td')
    description = (By.XPATH, '//table/tbody/tr[3]/td')
    title = (By.XPATH, '//table/tbody/tr[2]/td')
    id = (By.XPATH, '//table/tbody/tr[1]/td')


class ProductPage(BasePage):
    def verify_author(self, name):
        assert self.get(ProductPageLocators.author) == name

    def delete(self):
        self.click(ProductPageLocators.delete_product)
        self.driver.switch_to_alert().accept()

    def save_product_id(self):
        DataStoreFactory.scenario_data_store().put("product_id", self.get(ProductPageLocators.id))

    def verify_attribute(self, specifier, value):
        assert self.get(getattr(ProductPageLocators, specifier)) == value
