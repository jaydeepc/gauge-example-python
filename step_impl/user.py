from getgauge.python import step

from step_impl.driver import DriverFactory
from step_impl.pages.base_page import SignUpPage

page = SignUpPage(DriverFactory.driver)


@step("On signup page")
def navigate_to_sign_up_page():
    page.visit()


@step("Fill in and send registration form")
def fill_form():
    page.signup()
