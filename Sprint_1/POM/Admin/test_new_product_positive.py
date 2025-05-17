from selenium.webdriver.common.keys import Keys

from Sprint_1.POM.Admin.testdata_new_product import TESTDATA1
from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.NewProductPage import NewProductPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser


class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageLogin = LoginPageClass(self.browser)
        self.pageMain = MainPageClass(self.browser)
        self.pageProduct = NewProductPageClass(self.browser)
        self.pageLogin.get()
        # Login
        self.pageLogin.input_username().send_keys('Nyuszit%20Eszter')
        self.pageLogin.input_password().send_keys('Teszt1234?')
        self.pageLogin.button_login().click()
        # Navigates to New Product page.
        self.pageMain.button_newProduct().click()

    def teardown_method(self):
        self.browser.quit()

    def test_new_product(self):
        # Fills in form, saves new product and checks confirmation message.
        self.pageProduct.product_name().send_keys(TESTDATA1['Product Name'])
        self.pageProduct.product_category().click()
        self.pageProduct.product_categories(TESTDATA1['Categories']).click()
        self.pageProduct.product_category().send_keys(Keys.ESCAPE)
        self.pageProduct.product_price().send_keys(TESTDATA1['Price'])
        self.pageProduct.product_description().send_keys(TESTDATA1['Description'])

        self.pageProduct.save_product().click()

        assert "success" in self.pageProduct.overlay_text().text.lower()
        assert "unsuccessful" not in self.pageProduct.overlay_text().text.lower()
