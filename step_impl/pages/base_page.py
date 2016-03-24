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


class CustomerPage(BasePage):
    url = '{}customers/'.format(BasePage.admin_url)
    user_name = (By.ID, 'q_username')
    submit = (By.NAME, 'commit')
    result = (By.XPATH, '//table/tbody/tr[1]/td[3]')

    def search_user(self, username):
        self.driver.find_element(*self.user_name).send_keys(username)
        self.driver.find_element(*self.submit).click()

    def verify_user_listed(self, username):
        assert self.driver.find_element(*self.result).text == username

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
        self.driver.find_element(*self.user_name).send_keys(user_name)
        self.driver.find_element(*self.email).send_keys('{}@gmail.com'.format(user_name))
        self.driver.find_element(*self.password).send_keys('password')
        self.driver.find_element(*self.confirm_password).send_keys('password')
        self.driver.find_element(*self.submit).click()
        DataStoreFactory.scenario_data_store().put('current_user', user_name)

    def visit(self):
        self.driver.get(self.url)


class ProductListPage(BasePage):
    url = '{}products/'.format(BasePage.admin_url)
    title = (By.ID, 'q_title')
    submit = (By.NAME, "commit")
    first_product = (By.XPATH, '//table/tbody/tr[1]/td[1]/a')

    def search(self, name):
        self.driver.find_element(*self.title).send_keys(name)
        self.driver.find_element(*self.submit).click()

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
        self.driver.find_element(*self.title).send_keys(title)
        self.driver.find_element(*self.description).send_keys(desc)
        self.driver.find_element(*self.author).send_keys(author)
        self.driver.find_element(*self.price).send_keys(price)
        self.driver.find_element(*self.image).send_keys("not available")
        self.driver.find_element(*self.submit).click()

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
        self.driver.find_element(*self.author) == name

    def delete(self):
        self.driver.find_element(*self.delete_product).click()
        self.driver.switch_to_alert().accept()

    def save_product_id(self):
        DataStoreFactory.scenario_data_store().put("product_id", self.driver.find_element(*self.id).text)

    def verify_attribute(self, specifier, value):
        assert self.driver.find_element(*getattr(self, specifier)).text == value


class EditProductPage(BasePage):
    url = '{url}products/{{id}}/edit'.format(url=BasePage.admin_url)
    title = (By.ID, 'product_title')
    description = (By.ID, 'product_description')
    author = (By.ID, 'product_author')
    update_button = (By.NAME, "commit")

    def set_attribute_value(self, specifier, value):
        self.driver.find_element(*getattr(self, specifier)).clear()
        self.driver.find_element(*getattr(self, specifier)).send_keys(value)

    def save(self):
        self.driver.find_element(*self.update_button).click()

    def visit(self):
        self.driver.get(self.url.format(id=DataStoreFactory.scenario_data_store().get("product_id")))
