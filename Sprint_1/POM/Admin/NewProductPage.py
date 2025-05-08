from Sprint_1.POM.GeneralPage import GeneralPage
from selenium.webdriver.support.select import Select

class NewProductPageClass(GeneralPage):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/new-product'
        super().__init__(self.url, browser)

    def product_name(self):
        return self.webelement_by_id('input_pName')

    def product_category(self, index):
        return Select(self.webelement_by_id('input_Select')).select_by_index(index)

    def product_price(self):
        return self.webelement_by_id('input_pPrice')

    def product_description(self):
        return self.webelement_by_id('input_pDesc')

    def choose_an_image(self):
        return self.webelement_by_xpath('//button[text()=" Choose an image "]')

    def save_product(self):
        return self.webelement_by_xpath('//button[text()=" Save product "]')

    def cancel_button(self):
        return self.webelement_by_id('button_cancel')
