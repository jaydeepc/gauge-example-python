from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By

from step_impl.pages.base_page import BasePage


class ProductPage(BasePage):
    id = (By.XPATH, '//table/tbody/tr[1]/td')
    title = (By.XPATH, '//table/tbody/tr[2]/td')
    description = (By.XPATH, '//table/tbody/tr[3]/td')
    author = (By.XPATH, '//table/tbody/tr[4]/td')
    price = (By.XPATH, '//table/tbody/tr[5]/td')
    delete_product = (By.LINK_TEXT, 'Delete Product')

    def verify_author(self, name):
        assert self.get(self.author) == name

    def delete(self):
        self.click(self.delete_product)
        self.driver.switch_to_alert().accept()

    def save_product_id(self):
        DataStoreFactory.scenario_data_store().put("product_id", self.driver.find_element(*self.id).text)

    def verify_attribute(self, specifier, value):
        assert self.get(getattr(self, specifier)) == value
