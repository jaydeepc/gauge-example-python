from getgauge.python import step
from step_impl.pages.page_factory import PageFactory


@step('Create a product <table>')
def create_product(table):
    for row in table:
        PageFactory.create_page.visit()
        PageFactory.create_page.create(row[0], row[1], row[2], row[3])


@step('On product page')
def navigate_to_product_page():
    PageFactory.list_page.visit()


@step('Search for product <name>')
def search(name):
    PageFactory.list_page.search(name)


@step('Open description for product <name>')
def open_description(name):
    PageFactory.list_page.open_first_product()


@step('Verify product author as <author>')
def verify_author(author):
    PageFactory.product_page.verify_author(author)


@step('Delete this product')
def delete_product():
    PageFactory.product_page.delete()


@step('On new products page')
def navigate_to_new_products_page():
    PageFactory.create_page.visit()


@step('Verify product <specifier> as <value>')
def verify_product(specifier, value):
    PageFactory.product_page.verify_attribute(specifier, value)


@step('Find and store productId for <title>')
def find_store(title):
    PageFactory.list_page.visit()
    PageFactory.list_page.search(title)
    PageFactory.list_page.open_first_product()
    PageFactory.product_page.save_product_id()


@step('Open product edit page for stored productId')
def open_product_edit_page():
    PageFactory.edit_page.visit()


@step('Update product specifier to new value <table>')
def update_product(table):
    for row in table:
        PageFactory.edit_page.set_attribute_value(row[0], row[1])
        PageFactory.edit_page.save()


@step('Check product specifier has new value <table>')
def check_product(table):
    for row in table:
        PageFactory.product_page.verify_attribute(row[0], row[1])
