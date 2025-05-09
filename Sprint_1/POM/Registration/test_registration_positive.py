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

    def teardown_method(self):
        pass#self.pageMain.quit()

    def test_registration(self):
        helper = TestHelper(self.browser)

        username = self.pageRegistration.generate_username()
        email = f'{username}@teszt.hu'
        password = 'Teszt1234!'

        helper.register_user(username, email, password)
        helper.enable_user_in_db(email)
        helper.login_user(username, password)
