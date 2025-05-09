import csv
import pytest

from Sprint_1.POM.MainPage import MainPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from RegistrationPage import RegistrationPageClass
from Sprint_1.POM.Registration.TestHelper import TestHelper
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

def load_test_data():
    testdata_list = []
    path = "testdata_registration_negative_password.csv"
    with open(path, "r", encoding="utf-8") as dictfile:
        data = csv.DictReader(dictfile, delimiter=";")
        for row in data:
            testdata_list.append((row['password_1'], row['password_2']))
    return testdata_list


class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pageRegistration.get()
        self.username = self.pageRegistration.generate_username()
        self.e_mail = f"{self.username}@test.com"

    def teardown_method(self):
       self.pageMain.quit()

    @pytest.mark.parametrize("password_1, password_2", load_test_data())
    def test_registration_password(self, password_1, password_2):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys(self.username)
        self.pageRegistration.input_password_first().send_keys(password_1)
        self.pageRegistration.input_password_again().send_keys(password_2)
        self.pageRegistration.input_reg_email().click()

        assert self.pageRegistration.input_password_first().get_attribute("aria-invalid") == 'true'
        assert len(self.pageRegistration.password_checks()) < 4

    def test_registration_different_password(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys(self.username)
        self.pageRegistration.input_password_first().send_keys('Password_1')
        self.pageRegistration.input_password_again().send_keys('Password_2')
        self.pageRegistration.input_reg_email().click()

        assert self.pageRegistration.input_password_again().get_attribute("aria-invalid") == 'true'
        assert self.pageRegistration.error_message_different_pw().text == 'The passwords do not match'

    def test_registration_password_empty(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys(self.username)
        self.pageRegistration.input_password_first().click()
        self.pageRegistration.input_reg_email().click()

        assert self.pageRegistration.error_message_empty_pw().text == 'You must enter a password'

    def test_registration_password_with_accent_first_letter(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys(self.username)
        self.pageRegistration.input_password_first().send_keys('Ékezetes1!')
        self.pageRegistration.input_password_again().send_keys('Ékezetes1!')
        self.pageRegistration.input_reg_email().click()

        assert len(self.pageRegistration.password_checks()) == 4

    def test_registration_password_with_accent(self):
        helper = TestHelper(self.browser)
        username = self.username
        email = self.e_mail
        password = "Teszté1234!"

        helper.register_user(username, email, password)
        helper.enable_user_in_db(email)
        helper.login_user(username, password)

    def test_registration_password_with_space(self):
        helper = TestHelper(self.browser)
        username = self.username
        email = self.e_mail
        password = "Teszt 1234!"

        helper.register_user(username, email, password)
        helper.enable_user_in_db(email)
        helper.login_user(username, password)

