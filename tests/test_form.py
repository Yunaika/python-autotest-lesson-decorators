from helpers.model.app import sign_up_form, dashboard
from helpers.model.pages.sugn_up_form import given_sign_up_form_opened


def test_sign_up_form():
    given_sign_up_form_opened()
    (sign_up_form
     .fill_name('Julia', surname='Ivanova')
     .fill_email('murova47@gmail.com')
     .fill_password('qwerty')
     .submit()
     )
    dashboard.go_to_user_profile()
