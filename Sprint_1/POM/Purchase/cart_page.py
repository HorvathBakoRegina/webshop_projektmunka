from selenium.webdriver.common.by import By
from Sprint_1.POM.GeneralPage import GeneralPage

class MyCartPage(GeneralPage):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/registration'
        super().__init__(self.url, browser)

    def open_cart(self):
        self.browser.find_element(By.ID, "button_myCart").click()

    def continue_shopping(self):
        self.browser.find_element(By.XPATH, "//span[text()='Continue shopping']").click()

    def remove_item(self, index=0):
        try:
            minus_buttons = self.browser.find_elements(By.XPATH, "//button[contains(@class, 'minus_button')]")
            if minus_buttons:
                minus_buttons[index].click()

            x_buttons = self.browser.find_elements(By.XPATH, "//mat-icon[text()='close']")
            if x_buttons:
                x_buttons[index].click()
        except IndexError:
            print("Item not found at the given index.")

    def click_checkout(self):
        self.browser.find_element(By.XPATH, "//span[text()='Check out']").click()
