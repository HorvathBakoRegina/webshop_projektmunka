from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.RegistrationPage import RegistrationPageClass
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
        pass#self.pageMain.quit()

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