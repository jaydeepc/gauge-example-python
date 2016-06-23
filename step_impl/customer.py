from getgauge.python import step, DataStoreFactory

from step_impl.pages.page_factory import PageFactory


@step('On the customer page')
def navigate_to_customers_page():
    PageFactory.customer_page.visit()


@step('Search for customer <name>')
def search_user(name):
    PageFactory.customer_page.search_user(name)


@step('The customer <name> is listed')
def verify_user_is_listed(name):
    PageFactory.customer_page.verify_user_listed(name)


@step('Search for customers <table>')
def verify_customers(table):
    for row in table:
        PageFactory.customer_page.search_user(row[0])
        PageFactory.customer_page.verify_user_listed(row[0])


@step('Just registered customer is listed')
def verify_registered_customer_is_listed():
    PageFactory.customer_page.verify_user_listed(DataStoreFactory.scenario_data_store().get('current_user'))
