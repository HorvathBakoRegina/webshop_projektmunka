from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Sprint_1.POM.GeneralPage import GeneralPage


class MainPageClass(GeneralPage):

    def __init__(self):
        self.url = 'http://localhost:4200/'
        super().__init__(self.url)
        self.wait = WebDriverWait(self.browser, 7)

    def webelement_by_id(self, id):
        return self.wait.until(EC.element_to_be_clickable((By.ID, f'{id}')))

    def button_products(self):
        return self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Products')))

    def button_login(self):
        return self.webelement_by_id('regLogin')

    def button_myCart(self):
        return self.webelement_by_id('button_myCart')

    def button_location(self):
        return self.webelement_by_id('button_location')

    def button_search(self):
        return self.webelement_by_id('button_search')

    def button_filter(self):
        return self.webelement_by_id('mat-select-0')

    def button_filter_off(self):
        return self.webelement_by_id('filter-off')

    def list_products(self):
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@_ngcontent-qoa-c66]')))