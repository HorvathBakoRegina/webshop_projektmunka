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
        self.username = self.pageRegistration.generate_username('user')
        self.e_mail = f"{self.username}@test.com"

    def teardown_method(self):
        self.pageMain.quit()

    def test_registration(self):
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

    def test_registration_password_with_accent(self):
        username = self.username
        email = self.e_mail
        password = "Teszté1234!"

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert not self.pageLogin.error_message_wrong_user_pw().is_displayed()

    def test_registration_password_with_space(self):
        username = self.username
        email = self.e_mail
        password = "Teszt 1234!"

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert not self.pageLogin.error_message_wrong_user_pw().is_displayed()

    def test_registration_username_with_space(self):
        username = self.pageRegistration.generate_username_with_space("u")
        email = self.e_mail
        password = "Teszt1234!"

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert not self.pageLogin.error_message_wrong_user_pw().is_displayed()

    def test_registration_username_with_accent(self):
        username = self.pageRegistration.generate_username_with_accent('u')
        email = self.e_mail
        password = "Teszt1234!"

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert not self.pageLogin.error_message_wrong_user_pw().is_displayed()

    def test_registration_show_password(self):
        self.pageRegistration.input_password_first().send_keys('Teszt1234!')
        self.pageRegistration.input_password_again().send_keys('Teszt1234!')

        for element in self.pageRegistration.buttons_eye():
            element.click()
            assert element.text == 'visibility'
            element.click()
            assert element.text == 'visibility_off'

    def test_login_show_password(self):
        self.pageLogin.button_sign_in().click()
        self.pageLogin.input_password().send_keys('Teszt1234!')
        eye = self.pageLogin.button_eye()
        eye.click()
        assert eye.text == 'visibility'
        eye.click()
        assert eye.text == 'visibility_off'


