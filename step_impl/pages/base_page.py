import datetime
import os
import time

from getgauge.python import DataStoreFactory
from selenium.webdriver.common.by import By


class BasePage(object):
    url = os.getenv('APP_ENDPOINT')
    admin_url = '{}admin/'.format(url)

    def __init__(self, driver):
        self.driver = driver

    def click(self, element):
        self.driver.find_element(*element).click()

    def set(self, element, value):
        self.driver.find_element(*element).clear()
        self.driver.find_element(*element).send_keys(value)

    def get(self, element):
        return self.driver.find_element(*element).text


class CustomerPage(BasePage):
    url = '{}customers/'.format(BasePage.admin_url)
    user_name = (By.ID, 'q_username')
    submit = (By.NAME, 'commit')
    result = (By.XPATH, '//table/tbody/tr[1]/td[3]')

    def search_user(self, username):
        self.set(self.user_name, username)
        self.click(self.submit)

    def verify_user_listed(self, username):
        assert self.get(self.result) == username

    def visit(self):
        self.driver.get(self.url)


class SignUpPage(BasePage):
    url = '{}signup/'.format(BasePage.url)
    user_name = (By.ID, 'user_username')
    email = (By.ID, 'user_email')
    password = (By.ID, 'user_password')
    confirm_password = (By.ID, 'user_password_confirmation')
    submit = (By.NAME, "commit")

    def signup(self):
        user_name = 'user_{}'.format(time.mktime(datetime.datetime.now().timetuple()))
        self.set(self.user_name, user_name)
        self.set(self.email, '{}@gmail.com'.format(user_name))
        self.set(self.password, 'password')
        self.set(self.confirm_password, 'password')
        self.click(self.submit)
        DataStoreFactory.scenario_data_store().put('current_user', user_name)

    def visit(self):
        self.driver.get(self.url)


class ProductListPage(BasePage):
    url = '{}products/'.format(BasePage.admin_url)
    title = (By.ID, 'q_title')
    submit = (By.NAME, "commit")
    first_product = (By.XPATH, '//table/tbody/tr[1]/td[1]/a')

    def search(self, name):
        self.set(self.title, name)
        self.click(self.submit)

    def open_first_product(self):
        self.driver.find_element(*self.first_product).click()

    def visit(self):
        self.driver.get(self.url)


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
