import random
import csv

import pytest

from Sprint_1.POM.MainPage import MainPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from RegistrationPage import RegistrationPageClass
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

    def teardown_method(self):
        self.pageMain.quit()

    @pytest.mark.parametrize("password_1, password_2", load_test_data())
    def test_registration_password(self, password_1, password_2):
        username = self.pageRegistration.generate_username()
        email = f"{username}@test.com"

        self.pageRegistration.input_reg_email().send_keys(email)
        self.pageRegistration.input_reg_user().send_keys(username)
        self.pageRegistration.input_password_first().send_keys(password_1)
        self.pageRegistration.input_password_again().send_keys(password_2)
        self.pageRegistration.input_reg_email().click()

        assert (self.pageRegistration.input_password_first().get_attribute("aria-invalid") == 'true' or
                self.pageRegistration.input_password_again().get_attribute('aria-invalid') == 'true')

    def test_registration_password_empty(self):
        username = self.pageRegistration.generate_username()
        email = f"{username}@test.com"

        self.pageRegistration.input_reg_email().send_keys(email)
        self.pageRegistration.input_reg_user().send_keys(username)
        self.pageRegistration.input_password_first().click()
        self.pageRegistration.input_reg_email().click()

        assert self.pageRegistration.error_message_empty_pw().text == 'You must enter a password'
