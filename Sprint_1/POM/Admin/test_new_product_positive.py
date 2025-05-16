from Sprint_1.POM.Pages.LoginPage import LoginPageClass
from Sprint_1.POM.Pages.MainPage import MainPageClass
from Sprint_1.POM.Pages.NewProductPage import NewProductPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser


###
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageLogin = LoginPageClass(self.browser)
        self.pageMain = MainPageClass(self.browser)
        self.pageProduct = NewProductPageClass(self.browser)
        self.pageLogin.get()
        self.TESTDATA = {
            "Product Name": 'Hangdrum',
            "Categories": 3,
            "Price": 200,
            "Description": 'Steel tongue drum for Music Gift and Meditation, 14 inch, 440 Hz or 432 Hz',
            "Image URL": '',
        }
        #Login
        self.pageLogin.input_username().send_keys('Nyuszit%20Eszter')
        self.pageLogin.input_password().send_keys('Teszt1234?')
        self.pageLogin.button_login().click()
        #New Product page
        self.pageMain.button_newProduct().click()



    def teardown_method(self):
        # self.browser.quit()
        pass


    def test_new_product(self):

        self.pageProduct.product_name().send_keys(self.TESTDATA['Product Name'])
        # WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//mat-select[@id="input_Select"]'))).click()
        # WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//mat-option[@id="input_option"][1]'))).click()
        self.pageProduct.product_category().click()
        self.pageProduct.product_categories(self.TESTDATA['Categories']).click()

        self.pageProduct.product_category().send_keys(Keys.ESCAPE)


        self.pageProduct.product_price().send_keys(self.TESTDATA['Price'])
        self.pageProduct.product_description().send_keys(self.TESTDATA['Description'])


        # assert '//span[text()="Product save was successful"]'
        # self.pageProduct.save_product().click()


        # '//mat-select[@id="input_Select"]'
        # '//mat-option[@id="input_option"]'


        # pass





    #     self.pageRegistration.button_register().click()
    #
    #     assert self.pageRegistration.success_message().is_enabled()



        # class TestTC(object):
        #     def setup_method(self):
        #         options = Options()
        #         options.add_argument('--disable-search-engine-choice-screen')
        #         options.add_experimental_option("detach", True)
        #         self.browser = webdriver.Chrome(options=options)
        #         self.browser.maximize_window()
        #         self.browser.get(URL)
        #
        #     def teardown_method(self):
        #         self.browser.quit()
        #
        #     def test_tc1(self):
        #         pass