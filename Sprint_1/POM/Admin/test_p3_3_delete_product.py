from Sprint_1.POM.Admin.testdata_new_product_ID import Product_ID
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

    def test_delete_product_no(self):
        # Clicks "Delete" for a specific product, then cancels the action
        self.pageMain.button_delete(Product_ID).click()
        self.pageMain.button_delete_no().click()

        # Asserts that the product is not deleted from the product list
        product_id_list = []
        for i in self.pageMain.product_list():
            product_id_list.append(int(i.get_attribute("id")))
        assert (Product_ID) in product_id_list

    def test_delete_product_yes(self):
        # Clicks "Delete" for a specific product, then confirms the action
        self.pageMain.button_delete(Product_ID).click()
        self.pageMain.button_delete_yes().click()

        # Asserts that the product is deleted from the product list
        product_id_list = []
        for i in self.pageMain.product_list():
            product_id_list.append(int(i.get_attribute("id")))
        assert Product_ID not in product_id_list
