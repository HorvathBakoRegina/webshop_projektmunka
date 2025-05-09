import csv
import pytest

from Sprint_1.POM.MainPage import MainPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from RegistrationPage import RegistrationPageClass
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
        self.username = self.pageRegistration.generate_username()

    def teardown_method(self):
        self.pageMain.quit()

    @pytest.mark.parametrize("email", load_test_data())
    def test_registration_wrong_email(self, email):
        e_mail = f"{self.username}{email}"

        self.pageRegistration.input_reg_email().send_keys(e_mail)
        self.pageRegistration.input_reg_user().send_keys(self.username)

        assert self.pageRegistration.error_message_wrong_email().text == 'Not a valid email'

    def test_registration_wrong_email_2(self):
        self.pageRegistration.input_reg_email().send_keys('@teszt.hu')
        self.pageRegistration.input_reg_user().send_keys(self.username)

        assert self.pageRegistration.error_message_wrong_email().text == 'Not a valid email'

    def test_registration_exist_email(self):
        self.pageRegistration.input_reg_email().send_keys('backend.user@progmasters.hu')
        self.pageRegistration.input_reg_user().send_keys(self.username)
        self.pageRegistration.input_password_first().send_keys('Teszt1234!')
        self.pageRegistration.input_password_again().send_keys('Teszt1234!')
        self.pageRegistration.button_register().click()

        assert self.pageRegistration.error_message_exist_email().text == 'There is already a registered account with this email address.'

    def test_registration_without_email(self):
        self.pageRegistration.input_reg_email().send_keys('')
        self.pageRegistration.input_reg_user().send_keys(self.username)

        assert self.pageRegistration.error_message_wrong_email().text == 'You must enter your email address'

