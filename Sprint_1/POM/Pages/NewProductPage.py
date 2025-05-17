from Sprint_1.POM.Pages.GeneralPage import GeneralPageClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class NewProductPageClass(GeneralPageClass):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/new-product'
        super().__init__(self.url, browser)

    def product_name(self):
        return self.webelement_by_id('input_pName')

    def product_category(self):
        return self.webelement_by_id('input_Select')

    def product_categories(self, index):
        return self.webelement_by_xpath(f'//mat-option[@id="input_option"][{index}]')

    def product_price(self):
        return self.webelement_by_id('input_pPrice')

    def product_description(self):
        return self.webelement_by_id('input_pDesc')

    def choose_an_image(self):
        return self.webelement_by_classname('upload-btn')

    def save_product(self):
        return self.webelement_by_id('button_saveProduct')

    def cancel_button(self):
        return self.webelement_by_id('button_cancel')

    def overlay_text(self):
        return self.visibility_of_webelement_by_classname('mat-simple-snack-bar-content')
