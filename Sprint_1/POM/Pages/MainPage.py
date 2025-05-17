from Sprint_1.POM.Pages.GeneralPage import GeneralPageClass

class MainPageClass(GeneralPageClass):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/'
        super().__init__(self.url, browser)

    def logo(self):
        return self.webelement_by_id('logo-side')

    def button_products(self):
        return self.webelement_by_xpath('//span[text()=" Products "]')

    def button_newProduct(self):
        return self.webelement_by_id('button_newProduct')

    def button_Categories(self):
        return self.webelement_by_id('button_categories')

    def button_reLogin(self):
        return self.webelement_by_id('regLogin')

    def button_profile(self):
        return self.webelement_by_id('profile')

    def button_myCart(self):
        return self.webelement_by_id('button_myCart')

    def button_location(self):
        return self.webelement_by_id('button_location')

    def button_search(self):
        return self.webelement_by_id('button_search')

    def button_logOut(self):
        return self.webelement_by_id('button_logOut')

    def button_filter(self):
        return self.webelement_by_id('filter-on')

    def button_filter_off(self):
        return self.webelement_by_id('filter-off')

    def buttons_details(self):
        return self.webelements_by_id('button_details')

    def button_details(self, product_id):
        return self.webelement_by_xpath(f'//div[@id="{product_id}"]//button[@id="button_details"]')

    def buttons_add_cart(self):
        return self.webelements_by_id('button_addToCart')

    def button_add_cart(self, product_id):
        return self.webelement_by_xpath(f'//div[@id="{product_id}"]//button[@id="button_addToCart"]')

    def buttons_edit(self):
        return self.webelements_by_id('button_edit')

    def button_edit(self, product_id):
        return self.webelement_by_xpath(f'//div[@id="{product_id}"]//button[@id="button_edit"]')

    def buttons_delete(self):
        return self.webelements_by_id('button_delete')

    def button_delete(self, product_id):
        return self.webelement_by_xpath(f'//div[@id="{product_id}"]//button[@id="button_delete"]')

    def button_delete_no(self):
        return self.webelement_by_xpath('//button/span[text()= "No"]/..')

    def button_delete_yes(self):
        return self.webelement_by_xpath('//button/span[text()= "Yes"]/..')

    def product(self, product_id):
        return self.webelement_by_xpath(f'//div[@id="{product_id}"]')

    def product_list(self):
        return self.webelements_by_xpath('//div[@class="row"]/div')
