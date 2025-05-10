import csv
import pytest

from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.RegistrationPage import RegistrationPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

def load_test_data():
    testdata_list = []
    path = "testdata_registration_negative_password.csv"
    with open(path, "r", encoding="utf-8") as dictfile:
        data = csv.DictReader(dictfile, delimiter=";")
        for row in data:
            testdata_list.append((row['password']))
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

    @pytest.mark.parametrize("password", load_test_data())
    def test_registration_password(self, password):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys(self.username)
        self.pageRegistration.input_password_first().send_keys(password)
        self.pageRegistration.input_password_again().send_keys(password)
        self.pageRegistration.input_reg_email().click()

        assert self.pageRegistration.input_password_first().get_attribute("aria-invalid") == 'true'
        check = 0
        for element in self.pageRegistration.password_checks():
            if element.get_attribute('class') == 'mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color green':
                check += 1
        assert check < 4

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

        check = 0
        for element in self.pageRegistration.password_checks():
            if element.get_attribute('class') == 'mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color green':
                check += 1
        assert check == 4



