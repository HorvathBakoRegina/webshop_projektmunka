import csv
import pytest

from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.RegistrationPage import RegistrationPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

def load_test_data():
    testdata_list = []
    path = "testdata_registration_negative_email.csv"
    with open(path, "r", encoding="utf-8") as dictfile:
        data = csv.DictReader(dictfile, delimiter=";")
        for row in data:
            testdata_list.append((row['e-mail']))
    return testdata_list

class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pageRegistration.get()
        self.username = self.pageRegistration.generate_username('user')
        self.e_mail = f'{self.username}@teszt.hu'

    def teardown_method(self):
        self.pageMain.quit()

    @pytest.mark.parametrize("email", load_test_data())
    def test_registration_wrong_email(self, email):
        self.pageRegistration.input_reg_email().send_keys(email)
        self.pageRegistration.input_reg_user().send_keys(self.username)

        assert self.pageRegistration.error_message_wrong_email().text == 'Not a valid email'

    def test_registration_exist_email(self):
        username = self.username
        email = self.e_mail
        password = 'Teszt1234!'

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert self.pageMain.button_logOut().is_enabled()

        self.pageMain.button_logOut().click()
        self.pageLogin.button_create_account().click()

        self.pageRegistration.input_reg_email().send_keys(email)
        self.pageRegistration.input_reg_user().send_keys(f'1{self.username}')
        self.pageRegistration.input_password_first().send_keys(password)
        self.pageRegistration.input_password_again().send_keys(password)
        self.pageRegistration.button_register().click()

        assert self.pageRegistration.error_message_exist_email().text == 'There is already a registered account with this email address.'

    def test_registration_without_email(self):
        self.pageRegistration.input_reg_email().send_keys('')
        self.pageRegistration.input_reg_user().send_keys(self.username)

        assert self.pageRegistration.error_message_wrong_email().text == 'You must enter your email address'

