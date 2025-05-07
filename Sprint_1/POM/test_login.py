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
        self.pageMain.quit()
        self.pageLogin.quit()

    def test_login(self):
        self.pageLogin.input_email().send_keys('HB_Regi1')
        self.pageLogin.input_password().send_keys('Teszt1234!')
        self.pageLogin.button_login().click()

        assert self.pageMain.button_logOut().is_enabled()
