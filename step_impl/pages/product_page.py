from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class ProductPageLocators:
    DELETE_PRODUCT = (By.LINK_TEXT, 'Delete Product')
    PRICE = (By.XPATH, '//table/tbody/tr[5]/td')
    AUTHOR = (By.XPATH, '//table/tbody/tr[4]/td')
    DESCRIPTION = (By.XPATH, '//table/tbody/tr[3]/td')
    TITLE = (By.XPATH, '//table/tbody/tr[2]/td')
    ID = (By.XPATH, '//table/tbody/tr[1]/td')


class ProductPage(BasePage):
    def verify_author(self, name):
        assert self.get(ProductPageLocators.AUTHOR) == name

    def delete(self):
        self.click(ProductPageLocators.DELETE_PRODUCT)
        self.driver.switch_to_alert().accept()

    def save_product_id(self):
        DataStoreFactory.scenario_data_store().put('product_id', self.get(ProductPageLocators.ID))

    def verify_attribute(self, specifier, value):
        assert self.get(getattr(ProductPageLocators, specifier.upper())) == value
