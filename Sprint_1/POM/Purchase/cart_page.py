from Sprint_1.POM.Pages.GeneralPage import GeneralPage


class MyCartPageClass(GeneralPage):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/registration'
        super().__init__(self.url, browser)

    def open_cart(self):
        self.webelement_by_id("button_myCart").click()

    def continue_shopping(self):
        self.webelement_by_xpath("//span[text()='Continue shopping']").click()

    def remove_item(self):
        minus_buttons = self.webelement_by_xpath("//button[contains(@class, 'minus_button')]")
        x_buttons = self.webelement_by_xpath("//mat-icon[text()='close']")

    def click_checkout(self):
        self.webelement_by_xpath("//span[text()='Check out']").click()
