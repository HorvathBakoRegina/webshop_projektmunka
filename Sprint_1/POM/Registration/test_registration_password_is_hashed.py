from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.RegistrationPage import RegistrationPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser
import bcrypt

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
        password_bytes = password.encode()

        self.pageRegistration.register_user(username, email, password)
        assert self.pageRegistration.success_message().is_enabled()
        self.pageRegistration.enable_user_in_db(email)
        assert self.pageRegistration.is_user_enabled_in_db(email)
        self.pageLogin.login_user(username, password)
        assert self.pageLogin.button_login().is_enabled()

        hashed_password = (self.pageRegistration.get_user_password_by_email(email)).encode()

        assert password_bytes != hashed_password
        assert bcrypt.checkpw(password_bytes, hashed_password)

