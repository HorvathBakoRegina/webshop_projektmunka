from Sprint_1.POM.Pages.GeneralPage import GeneralPageClass
from Sprint_1.POM.Pages.LoginPage import LoginPageClass

class PurchasePageClass(GeneralPageClass):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/registration'
        super().__init__(self.url, browser)

    def products_list(self):
        return self.webelement_by_xpath(
            '//div[contains(@class, "col") and contains(@class, "ng-star-inserted") and @id]')

    def product_add_to_cart(self, index=0):
        self.webelements_by_id('button_addToCart')[index].click()

    def open_cart(self):
        self.webelement_by_id("button_myCart").click()

    def click_checkout(self):
        self.webelement_by_xpath("//span[text()='Check out']").click()

    def back_to_cart(self):
        self.webelement_by_xpath("//span[text()='Back to the cart ']").click()

    def form_input_error_message(self):
        return self.webelement_by_xpath('//form/div/mat-error')

    def click_next(self):
        next_buttons = self.webelements_by_classname("next_btn")
        for btn in next_buttons:
            if btn.is_displayed() and btn.is_enabled():
                btn.click()
                break

    def enter_customer_details(self, name, email, phone):
        self.webelement_by_xpath('//input[@id="formName_input"]').send_keys(name)
        email_input = self.webelement_by_xpath('//input[@id="formEmail_input"]')
        email_input.clear()
        email_input.send_keys(email)
        self.webelement_by_xpath('//input[@id="formPhoneNumber_input"]').send_keys(phone)

    def billing_details(self, name, zip_code, city, street_nr):
        self.webelement_by_xpath('//input[@id="formName1_input"]').send_keys(name)
        self.webelement_by_xpath('//input[@id="formZIP_input"]').send_keys(zip_code)
        self.webelement_by_xpath('//input[@id="city_input"]').send_keys(city)
        self.webelement_by_xpath('//input[@id="adress_input"]').send_keys(street_nr)
        self.click_next()

    def shipping_details(self, name, zip_code, city, street_nr):
        self.webelement_by_xpath('//input[@id="formName1_input"]').send_keys(name)
        self.webelement_by_xpath('//input[@id="formZIP_input"]').send_keys(zip_code)
        self.webelement_by_xpath('//input[@id="city_input"]').send_keys(city)
        self.webelement_by_xpath('//input[@id="adress_input"]').send_keys(street_nr)
        self.click_next()

    def delivery_info(self, note="Ring the Bell"):
        text_area = self.webelement_by_id('delivery_input').send_keys(note)
        self.click_next()

    def payment_opt(self, method="card"):
        if method == "cash":
            self.webelement_by_id('mat-radio-14').click()
        else:
            self.webelement_by_id('mat-radio-15').click()
        self.webelement_by_classname("send_btn").click()

    def get_payment_confirmation_message(self):
        actual_message = self.webelement_by_xpath("//p[contains(text(), 'The order has been sent')]").text
        assert "The order has been sent" in actual_message, f"Expected message 'The order has been sent', but got: {actual_message}"
        return actual_message
