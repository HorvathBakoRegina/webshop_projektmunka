from datetime import datetime
import mysql.connector


from Sprint_1.POM.Pages.GeneralPage import GeneralPageClass

class RegistrationPageClass(GeneralPageClass):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/registration'
        super().__init__(self.url, browser)

    def input_reg_email(self):
        return self.webelement_by_formcontrolname('email')

    def input_reg_user(self):
        return self.webelement_by_formcontrolname('userName')

    def input_password_first(self):
        return self.webelement_by_formcontrolname('password')

    def input_password_again(self):
        return self.webelement_by_formcontrolname('confirmPassword')

    def button_register(self):
        return self.webelement_by_xpath('//button[@type="submit"]')

    def success_message(self):
        return self.webelement_by_xpath('//div[@class="success_message ng-star-inserted"]')

    def password_checks(self):
        return self.webelements_by_xpath('//div[@id="checkers"]//mat-icon')

    def error_message_empty_pw(self):
        return self.error_message(self.input_password_first())

    def error_message_different_pw(self):
        return self.error_message(self.input_password_again())

    def error_message_wrong_email(self):
        return self.error_message(self.input_reg_email())

    def error_message_exist_email(self):
        return self.webelement_by_xpath('//form/div/mat-error')

    def error_message_wrong_username(self):
        return self.error_message(self.input_reg_user())

    def generate_username(self, prefix):
        now = datetime.now()
        timestamp_str = now.strftime("%d%m%y_%H%M%S")
        tenth = str(now.microsecond)[0]
        return f"{prefix}_{timestamp_str}{tenth}"

    def generate_username_with_accent(self, prefix):
        now = datetime.now()
        timestamp_str = now.strftime("%H%M%S")
        tenth = str(now.microsecond)[0]
        return f"é{prefix}{timestamp_str}{tenth}"

    def register_user(self, username: str, email: str, password: str):
        self.input_reg_email().send_keys(email)
        self.input_reg_user().send_keys(username)
        self.input_password_first().send_keys(password)
        self.input_password_again().send_keys(password)
        self.button_register().click()

    def enable_user_in_db(self, email):
        connection = mysql.connector.connect(
            user="root",
            password="test1234",
            host="127.0.0.1",
            database="webshop"
        )
        cursor = connection.cursor(dictionary=True)
        update = "UPDATE custom_user SET enabled = %s WHERE email = %s;"
        values = [1, email]
        cursor.execute(update, values)
        connection.commit()
        cursor.close()
        connection.close()

    def is_user_enabled_in_db(self, email):
        connection = mysql.connector.connect(
            user="root",
            password="test1234",
            host="127.0.0.1",
            database="webshop"
        )
        cursor = connection.cursor(dictionary=True)
        query = "SELECT enabled FROM custom_user WHERE email = %s;"
        cursor.execute(query, [email])
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result is not None:
            return result['enabled'] == 1
        return False


