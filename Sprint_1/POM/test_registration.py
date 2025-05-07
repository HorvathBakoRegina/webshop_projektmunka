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