from Sprint_1.POM.GeneralPage import GeneralPage

class LoginPageClass(GeneralPage):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/login/'
        super().__init__(self.url, browser)

    def button_create_account(self):
        return self.webelement_by_xpath('//button[text()="Create Account"]')

    def button_sign_in(self):
        return self.webelement_by_xpath('//button[text()="Sign In"]')

    def input_email(self):
        return self.webelement_by_id('username_input')

    def input_password(self):
        return self.webelement_by_id('password_input')

    def button_login(self):
        return self.webelement_by_xpath('//button[@type="submit"]')