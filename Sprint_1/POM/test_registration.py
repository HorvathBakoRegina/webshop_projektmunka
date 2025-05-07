from MainPage import MainPageClass
from LoginPage import LoginPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

class TestTC(object):
    def setup_method(self):
        browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(browser)
        self.pageLogin = LoginPageClass(browser)
        self.pageLogin.get()

    def teardown_method(self):
        pass#self.pageMain.quit()

    def test_login(self):
        self.pageLogin.button_create_account().click()
        self.pageLogin.input_reg_email().send_keys('valami@valami.hu')
        self.pageLogin.input_reg_user().send_keys('random_nev')
        self.pageLogin.input_password_first().send_keys('Teszt1234!')
        self.pageLogin.input_password_again().send_keys('Teszt1234!')
        self.pageLogin.button_register().click()
