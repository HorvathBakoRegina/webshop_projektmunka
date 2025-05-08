from selenium.webdriver.common.by import By
from Sprint_1.POM.GeneralPage import GeneralPage

class PurchasePage(GeneralPage):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/registration'
        super().__init__(self.url, browser)

    def products_list(self):
        return self.browser.find_elements(By.XPATH, '//div[contains(@class, "col") and contains(@class, "ng-star-inserted") and @id]')

    def product_add_to_cart(self, index=0):
        self.browser.find_elements(By.ID, 'button_addToCart')[index].click()

    def open_cart(self):
        self.browser.find_element(By.ID, "button_myCart").click()

    def click_checkout(self):
        self.browser.find_element(By.XPATH, "//span[text()='Check out']").click()

    def back_to_cart(self):
        self.browser.find_element(By.XPATH, "//span[text()='Back to the cart ']").click()

    def click_next(self):
        self.browser.find_element(By.CLASS_NAME, "next_btn").click()

    def enter_customer_details(self, name, email, phone):
        self.browser.find_element(By.XPATH, '//input[@id="formName_input"]').send_keys(name)
        self.browser.find_element(By.XPATH, '//input[@id="formEmail_input"]').send_keys(email)
        self.browser.find_element(By.XPATH, '//input[@id="formPhoneNumber_input"]').send_keys(phone)

    def billing_details(self, name, zip_code, city, street_nr):
        self.browser.find_element(By.XPATH, '//input[@id="formName1_input"]').send_keys(name)
        self.browser.find_element(By.XPATH, '//input[@id="formZIP_input"]').send_keys(zip_code)
        self.browser.find_element(By.XPATH, '//input[@id="city_input"]').send_keys(city)
        self.browser.find_element(By.XPATH, '//input[@id="adress_input"]').send_keys(street_nr)
        self.click_next()

    def shipping_details(self, name, zip_code, city, street_nr):
        self.browser.find_element(By.XPATH, '//input[@id="formName1_input"]').send_keys(name)
        self.browser.find_element(By.XPATH, '//input[@id="formZIP_input"]').send_keys(zip_code)
        self.browser.find_element(By.XPATH, '//input[@id="city_input"]').send_keys(city)
        self.browser.find_element(By.XPATH, '//input[@id="adress_input"]').send_keys(street_nr)
        self.click_next()

    def delivery_info(self, note="Ring the Bell"):
        text_area = self.browser.find_element(By.ID, 'delivery_input').send_keys(note)
        self.click_next()

    def payment_opt(self, method="card"):
        if method == "cash":
            self.browser.find_element(By.ID, 'mat-radio-14').click()
        else:
            self.browser.find_element(By.ID, 'mat-radio-15').click()
        self.browser.find_element(By.CLASS_NAME, "send_btn").click()

    def get_payment_confirmation_message(self):
        actual_message = self.browser.find_element(By.XPATH, "//p[contains(text(), 'The order has been sent')]").text
        assert "The order has been sent" in actual_message, f"Expected message 'The order has been sent', but got: {actual_message}"
        return actual_message
