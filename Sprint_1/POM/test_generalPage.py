from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from MainPage import MainPageClass


class TestTC(object):
    def setup_method(self):
        self.page = MainPageClass()
        self.page.get()

    def teardown_method(self):
        self.page.quit()

    def test_kattint(self):
        self.page.button_products().click()

    def test_kattint_2(self):
        self.page.button_myCart().click()

    def test_szamol(self):
        print(self.page.list_products())