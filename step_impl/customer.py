from getgauge.python import step, DataStoreFactory

from step_impl.driver.driver import DriverFactory
from step_impl.pages.customer_page import CustomerPage

page = CustomerPage(DriverFactory.driver)


@step("On the customer page")
def navigate_to_customers_page():
    page.visit()


@step("Search for customer <name>")
def search_user(name):
    page.search_user(name)


@step("The customer <name> is listed")
def verify_user_is_listed(name):
    page.verify_user_listed(name)


@step("Search for customers <table>")
def verify_customers(table):
    for row in table:
        page.search_user(row[0])
        page.verify_user_listed(row[0])


@step("Just registered customer is listed")
def verify_registered_customer_is_listed():
    page.verify_user_listed(DataStoreFactory.scenario_data_store().get('current_user'))
