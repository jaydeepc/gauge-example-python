from getgauge.python import before_suite, after_suite
from selenium import webdriver

from step_impl.pages.create_product_page import CreateProductPage
from step_impl.pages.customer_page import CustomerPage
from step_impl.pages.edit_product_page import EditProductPage
from step_impl.pages.product_list_page import ProductListPage
from step_impl.pages.product_page import ProductPage
from step_impl.pages.signup_page import SignUpPage


class PageFactory:
    driver = None
    list_page = None
    create_page = None
    product_page = None
    edit_page = None
    customer_page = None
    user_page = None


@before_suite
def init():
    PageFactory.driver = webdriver.Firefox()
    PageFactory.list_page = ProductListPage(PageFactory.driver)
    PageFactory.create_page = CreateProductPage(PageFactory.driver)
    PageFactory.product_page = ProductPage(PageFactory.driver)
    PageFactory.edit_page = EditProductPage(PageFactory.driver)
    PageFactory.customer_page = CustomerPage(PageFactory.driver)
    PageFactory.user_page = SignUpPage(PageFactory.driver)


@after_suite
def close():
    PageFactory.driver.close()
