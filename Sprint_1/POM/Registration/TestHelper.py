import mysql.connector
from RegistrationPage import RegistrationPageClass
from Sprint_1.POM.LoginPage import LoginPageClass
from Sprint_1.POM.MainPage import MainPageClass

class TestHelper():
    def __init__(self, browser):
        self.browser = browser
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)

    def register_user(self, username: str, email: str, password: str):
        self.pageRegistration.input_reg_email().send_keys(email)
        self.pageRegistration.input_reg_user().send_keys(username)
        self.pageRegistration.input_password_first().send_keys(password)
        self.pageRegistration.input_password_again().send_keys(password)
        self.pageRegistration.button_register().click()
        assert self.pageRegistration.success_message().is_enabled()

    def enable_user_in_db(self, email):
        connection = mysql.connector.connect(
            user="root",
            password="test1234",
            host="127.0.0.1",
            database="webshop"
        )
        assert connection.is_connected()
        cursor = connection.cursor(dictionary=True)
        update = "UPDATE custom_user SET enabled = %s WHERE email = %s;"
        values = [1, email]
        cursor.execute(update, values)
        connection.commit()
        cursor.close()
        connection.close()

    def login_user(self, username: str, password: str):
        self.pageLogin.button_sign_in().click()
        self.pageLogin.input_username().send_keys(username)
        self.pageLogin.input_password().send_keys(password)
        self.pageLogin.button_login().click()
        assert self.pageMain.button_logOut().is_enabled()