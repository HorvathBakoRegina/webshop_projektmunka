from Sprint_1.POM.MainPage import MainPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from RegistrationPage import RegistrationPageClass
from Sprint_1.POM.Registration.TestHelper import TestHelper
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pageRegistration.get()
        self.e_mail = f"{self.pageRegistration.generate_username()}@teszt.hu"

    def teardown_method(self):
        self.pageMain.quit()

    def test_registration_username_with_space(self):
        helper = TestHelper(self.browser)

        username = f"{helper.pageRegistration.generate_username()} {helper.pageRegistration.generate_username()}"
        email = self.e_mail
        password = "Teszt1234!"

        helper.register_user(username, email, password)
        helper.enable_user_in_db(email)
        helper.login_user(username, password)

    def test_registration_username_with_accent(self):
        helper = TestHelper(self.browser)

        username = f'{self.pageRegistration.generate_username_accent()}{self.pageRegistration.generate_username()}'
        email = self.e_mail
        password = "Teszt1234!"

        helper.register_user(username, email, password)
        helper.enable_user_in_db(email)
        helper.login_user(username, password)

    def test_registration_exist_username(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys('user')
        self.pageRegistration.input_password_first().send_keys('Teszt1234!')
        self.pageRegistration.input_password_again().send_keys('Teszt1234!')
        self.pageRegistration.button_register().click()

        assert self.pageRegistration.error_message_exist_email().text == 'Username is already in use.'

    def test_registration_without_username(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys('')
        self.pageRegistration.input_password_first().click()

        assert self.pageRegistration.error_message_wrong_username().text == 'You must enter the name'

    def test_registration_short_username(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys('use')
        self.pageRegistration.input_password_first().click()

        assert self.pageRegistration.error_message_wrong_username().text == 'The length should be minimum 4 characters'

    def test_registration_long_username(self):
        self.pageRegistration.input_reg_email().send_keys(self.e_mail)
        self.pageRegistration.input_reg_user().send_keys('usernameusernameusernameusername')
        self.pageRegistration.input_password_first().click()

        assert self.pageRegistration.error_message_wrong_username().text == 'The length should be maximum 20 characters'