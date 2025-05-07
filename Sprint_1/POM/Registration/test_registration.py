import time

from Sprint_1.POM.MainPage import MainPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from TemporaryEmailPage import TemporaryEmailPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

TESTDATA = {
    "E-mail": '',
    "Username": 'barmi8589',
    "Password": 'Test1234!',
}

class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)
        self.pageTempEmail = TemporaryEmailPageClass(self.browser)
        self.pageTempEmail.get()

    def teardown_method(self):
        pass#self.pageMain.quit()

    def test_login(self):
        time.sleep(5)
        TESTDATA["E-mail"] = self.pageTempEmail.temporary_email().get_attribute('value')
        print(TESTDATA["E-mail"])
        self.browser.switch_to.new_window()
        self.pageLogin.get()

        email_tab = self.browser.window_handles[0]

        self.pageLogin.button_create_account().click()
        self.pageLogin.input_reg_email().send_keys(TESTDATA['E-mail'])
        self.pageLogin.input_reg_user().send_keys(TESTDATA['Username'])
        self.pageLogin.input_password_first().send_keys(TESTDATA['Password'])
        self.pageLogin.input_password_again().send_keys(TESTDATA['Password'])
        self.pageLogin.button_register().click()

        assert self.pageLogin.success_message().is_enabled()

        self.browser.switch_to.window(email_tab)

        self.pageTempEmail.incoming_email().click()

        self.browser.switch_to.frame(self.pageTempEmail.iframe())

        link = self.pageTempEmail.activation_link()
        activation_url = link.get_attribute("href")
        self.browser.get(activation_url)

        self.pageLogin.input_username().send_keys(TESTDATA['Username'])
        self.pageLogin.input_password().send_keys(TESTDATA['Password'])
        self.pageLogin.button_login().click()

        assert self.pageMain.button_logOut().is_enabled()


