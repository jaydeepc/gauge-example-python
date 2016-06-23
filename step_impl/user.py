from getgauge.python import step

from step_impl.pages.page_factory import PageFactory


@step('On signup page')
def navigate_to_sign_up_page():
    PageFactory.user_page.visit()


@step('Fill in and send registration form')
def fill_form():
    PageFactory.user_page.signup()
