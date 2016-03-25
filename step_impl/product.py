from getgauge.python import step

from step_impl.driver.driver import DriverFactory
from step_impl.pages.create_product_page import CreateProductPage
from step_impl.pages.edit_product_page import EditProductPage
from step_impl.pages.product_list_page import ProductListPage
from step_impl.pages.product_page import ProductPage

list_page = ProductListPage(DriverFactory.driver)
create_page = CreateProductPage(DriverFactory.driver)
product_page = ProductPage(DriverFactory.driver)
edit_page = EditProductPage(DriverFactory.driver)


@step('Create a product <table>')
def create_product(table):
    for row in table:
        create_page.visit()
        create_page.create(row[0], row[1], row[2], row[3])


@step('On product page')
def navigate_to_product_page():
    list_page.visit()


@step('Search for product <name>')
def search(name):
    list_page.search(name)


@step('Open description for product <name>')
def open_description(name):
    list_page.open_first_product()


@step('Verify product author as <author>')
def verify_author(author):
    product_page.verify_author(author)


@step('Delete this product')
def delete_product():
    product_page.delete()


@step('On new products page')
def navigate_to_new_products_page():
    create_page.visit()


@step('Verify product <specifier> as <value>')
def verify_product(specifier, value):
    product_page.verify_attribute(specifier, value)


@step('Find and store productId for <title>')
def find_store(title):
    list_page.visit()
    list_page.search(title)
    list_page.open_first_product()
    product_page.save_product_id()


@step('Open product edit page for stored productId')
def open_product_edit_page():
    edit_page.visit()


@step('Update product specifier to new value <table>')
def update_product(table):
    for row in table:
        edit_page.set_attribute_value(row[0], row[1])
        edit_page.save()


@step('Check product specifier has new value <table>')
def check_product(table):
    for row in table:
        product_page.verify_attribute(row[0], row[1])
