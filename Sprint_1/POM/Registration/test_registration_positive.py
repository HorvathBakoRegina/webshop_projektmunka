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
        self.username = self.pageRegistration.generate_username()
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
        assert self.pageMain.button_logOut().is_enabled()

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
        assert self.pageMain.button_logOut().is_enabled()

    def test_registration_username_with_space(self):
        username = f"{self.pageRegistration.generate_username()} {self.pageRegistration.generate_username()}"
        email = self.e_mail
        password = "Teszt1234!"

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert self.pageMain.button_logOut().is_enabled()

    def test_registration_username_with_accent(self):
        username = f'{self.pageRegistration.generate_username_accent()}{self.pageRegistration.generate_username()}'
        email = self.e_mail
        password = "Teszt1234!"

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()
        assert self.pageMain.button_logOut().is_enabled()
