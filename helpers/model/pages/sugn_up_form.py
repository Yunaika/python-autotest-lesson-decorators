import allure

from helpers.allure.report import step


@step
def given_sign_up_form_opened():
    ...


class SignUpForm:

    @step
    def fill_name(self, first_name, surname):
        pass
        return self

    @step
    def fill_email(self, value):
        pass
        return self

    @step
    def fill_password(self, value):
        pass
        return self

    @step
    def submit(self):
        pass
        return self
