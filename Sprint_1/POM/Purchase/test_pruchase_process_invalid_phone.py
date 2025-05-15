from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.RegistrationPage import RegistrationPageClass
from Sprint_1.POM.Pages.Purchase_Page import PurchasePageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser


class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageMain = MainPageClass(self.browser)
        self.pageLogin = LoginPageClass(self.browser)
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pagePurchase = PurchasePageClass(self.browser)
        self.pageRegistration.get()
        self.username = self.pageRegistration.generate_username('user')
        self.e_mail = f"{self.username}@test.com"

    def teardown_method(self):
        self.browser.quit()

    def test_purchase_process_invalid_phone(self):
        # 2. Login
        self.pageLogin.get()
        self.pageLogin.login_user(username="Mercedesz", password="Teszt1234!")

        assert self.pageMain.button_logOut().is_displayed()

        # 3. Purchase End to End
        test_data = {
            "customer": {
                "name": "Búza Virág",
                "email": "xehew29186@daupload.com",
                "phone": "0612345"
            },
            "billing_address": {
                "name": "Búza Virág",
                "zip": "1234",
                "city": "Budapest",
                "street": "Fő utca 1."
            },
            "shipping_address": {
                "name": "Búza Virág",
                "zip": "1234",
                "city": "Budapest",
                "street": "Fő utca 1."
            },
            "delivery_note": "Kérem, csengetni.",
            "payment_method": "card"
        }
        # Add Product
        self.pagePurchase.products_list()
        add_more_products = [0, 1, 2]
        for index in add_more_products:
            self.pagePurchase.product_add_to_cart(index=index)
        self.pagePurchase.open_cart()
        assert self.pagePurchase.get_cart_item_count() == 3
        self.pagePurchase.click_checkout()

        # Order Details
        self.pagePurchase.enter_customer_details(
            test_data["customer"]["name"],
            test_data["customer"]["email"],
            test_data["customer"]["phone"]
        )
        assert self.pagePurchase.form_input_error_message()
        self.pagePurchase.click_next()

        # Billing Details
        self.pagePurchase.billing_details(
            test_data["billing_address"]["name"],
            test_data["billing_address"]["zip"],
            test_data["billing_address"]["city"],
            test_data["billing_address"]["street"]
        )
        self.pagePurchase.click_next()
        assert not self.pagePurchase.form_input_error_message()

        # Shipping Details
        self.pagePurchase.shipping_details(
            test_data["shipping_address"]["name"],
            test_data["shipping_address"]["zip"],
            test_data["shipping_address"]["city"],
            test_data["shipping_address"]["street"]
        )
        assert not self.pagePurchase.form_input_error_message()
        self.pagePurchase.click_next()

        # Delivery Information
        self.pagePurchase.delivery_info(note=test_data["delivery_note"])
        assert not self.pagePurchase.form_input_error_message()
        self.pagePurchase.click_next()

        # Payment Options
        self.pagePurchase.payment_opt(method=test_data["payment_method"])
        assert self.pagePurchase.send_button().is_displayed()
        self.pagePurchase.send_button()

        # Payment Confirmation
        confirmation_message = self.pagePurchase.get_payment_confirmation_message()
        assert "The order has been sent" in confirmation_message