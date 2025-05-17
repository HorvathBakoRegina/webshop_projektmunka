from selenium.webdriver.common.keys import Keys

from Sprint_1.POM.Admin.testdata_new_product import TESTDATA1, TESTDATA2
from Sprint_1.POM.Pages.DetailsPage import DetailsPageClass
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
        self.pageDetails = DetailsPageClass(self.browser)
        self.pageLogin.get()
        # Login
        self.pageLogin.input_username().send_keys('Nyuszit%20Eszter')
        self.pageLogin.input_password().send_keys('Teszt1234?')
        self.pageLogin.button_login().click()

    def teardown_method(self):
        self.browser.quit()

    def test_update_product(self):
        # Opens the edit page of a specific product by product ID
        self.pageMain.button_edit(TESTDATA2['Product ID']).click()

        # Clears previously given input, enters and saves new input
        self.pageProduct.product_name().clear()
        self.pageProduct.product_name().send_keys(TESTDATA2['Product Name'])

        self.pageProduct.product_category().click()
        self.pageProduct.product_categories(TESTDATA1['Categories']).click()
        self.pageProduct.product_categories(TESTDATA2['Categories']).click()
        category_name = (self.pageProduct.product_categories(TESTDATA2['Categories'])).text  # saves category name
        self.pageProduct.product_category().send_keys(Keys.ESCAPE)

        self.pageProduct.product_price().clear()
        self.pageProduct.product_price().send_keys(TESTDATA2['Price'])

        self.pageProduct.product_description().clear()
        self.pageProduct.product_description().send_keys(TESTDATA2['Description'])

        self.pageProduct.save_product().click()

        # Opens the details page of the modified product and checks if the data matches the new input
        self.pageMain.button_details(TESTDATA2['Product ID']).click()
        assert TESTDATA2['Product Name'] in self.pageDetails.product_name_detail().text
        assert category_name in self.pageDetails.product_category_detail().text
        assert TESTDATA2['Price'] in self.pageDetails.product_price_detail().text
        assert TESTDATA2['Description'] in self.pageDetails.product_description_detail().text
