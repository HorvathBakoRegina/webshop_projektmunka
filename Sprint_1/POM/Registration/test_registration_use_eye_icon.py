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

    def teardown_method(self):
        self.pageMain.quit()

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