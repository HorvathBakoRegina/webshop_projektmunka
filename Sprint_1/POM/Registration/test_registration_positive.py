import mysql.connector
import random

from Sprint_1.POM.MainPage import MainPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from RegistrationPage import RegistrationPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

length = 10
username = ''.join(random.choice(characters) for _ in range(length))

TESTDATA = {
    "E-mail": f'{username}@test.com',
    "Username": f'{username}',
    "Password": 'Test1234!',
}

class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pageRegistration.get()

    def teardown_method(self):
        self.pageMain.quit()

    def test_registration(self):
        self.pageRegistration.input_reg_email().send_keys(TESTDATA['E-mail'])
        self.pageRegistration.input_reg_user().send_keys(TESTDATA['Username'])
        self.pageRegistration.input_password_first().send_keys(TESTDATA['Password'])
        self.pageRegistration.input_password_again().send_keys(TESTDATA['Password'])
        self.pageRegistration.button_register().click()

        assert self.pageRegistration.success_message().is_enabled()

        connection = mysql.connector.connect(user="root",
                                    password="test1234",
                                    host="127.0.0.1",
                                    database="webshop")

        assert connection.is_connected()

        db_email = TESTDATA["E-mail"]
        kurzor = connection.cursor(dictionary=True)

        update = "UPDATE custom_user SET enabled = %s WHERE email = %s;"
        values = [1, f'{db_email}']

        kurzor.execute(update, values)
        connection.commit()

        self.pageLogin.button_sign_in().click()

        self.pageLogin.input_username().send_keys(TESTDATA['Username'])
        self.pageLogin.input_password().send_keys(TESTDATA['Password'])
        self.pageLogin.button_login().click()

        assert self.pageMain.button_logOut().is_enabled()