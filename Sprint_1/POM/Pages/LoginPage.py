from Sprint_1.POM.Pages.GeneralPage import GeneralPageClass

class LoginPageClass(GeneralPageClass):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/login/'
        super().__init__(self.url, browser)

    def button_create_account(self):
        return self.webelement_by_xpath('//button[text()="Create Account"]')

    def button_sign_in(self):
        return self.webelement_by_xpath('//button[text()="Sign In"]')

    def input_username(self):
        return self.webelement_by_id('username_input')

    def input_password(self):
        return self.webelement_by_id('password_input')

    def button_eye(self):
        return self.webelement_by_xpath('//div/button[@mat-icon-button]/span/mat-icon')

    def button_login(self):
        return self.webelement_by_xpath('//button[@type="submit"]')

    def error_message_wrong_user_pw(self):
        return self.webelement_by_xpath('//form/div/mat-error')

    def login_user(self, username: str, password: str):
        self.button_sign_in().click()
        self.input_username().send_keys(username)
        self.input_password().send_keys(password)
        self.button_login().click()
