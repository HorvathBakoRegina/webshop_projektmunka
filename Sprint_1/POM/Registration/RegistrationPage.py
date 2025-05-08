from Sprint_1.POM.GeneralPage import GeneralPage

class RegistrationPageClass(GeneralPage):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/registration'
        super().__init__(self.url, browser)

    def input_reg_email(self):
        return self.webelement_by_xpath('//input[@formcontrolname="email"]')

    def input_reg_user(self):
        return self.webelement_by_xpath('//input[@formcontrolname="userName"]')

    def input_password_first(self):
        return self.webelement_by_xpath('//input[@formcontrolname="password"]')

    def input_password_again(self):
        return self.webelement_by_xpath('//input[@formcontrolname="confirmPassword"]')

    def button_register(self):
        return self.webelement_by_xpath('//button[@type="submit"]')

    def success_message(self):
        return self.webelement_by_xpath('//div[@class="success_message ng-star-inserted"]')

    def password_checks(self):
        return self.webelements_by_xpath('//mat-icon[@class="mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color green"]')

    def error_message_empty_pw(self):
        return self.webelement_by_xpath('//input[@formcontrolname="password"]/../../../div[3]/div/mat-error')
