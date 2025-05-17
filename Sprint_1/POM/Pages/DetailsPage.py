from Sprint_1.POM.Pages.GeneralPage import GeneralPageClass


class DetailsPageClass(GeneralPageClass):
    def __init__(self, browser):
        self.url = 'http://localhost:4200/product-details/'
        super().__init__(self.url, browser)

    def product_name_detail(self):
        return self.visibility_of_webelement_by_id('product-name')

    def product_category_detail(self):
        return self.webelement_by_id('category')

    def product_price_detail(self):
        return self.visibility_of_webelement_by_xpath('//h2[contains(text(), "Price")]')

    def product_description_detail(self):
        return self.visibility_of_webelement_by_xpath('//strong[contains(text(), "Description")]/..')

    def product_image_detail(self):
        return self.visibility_of_webelement_by_classname('product-list-item__image')

    def add_to_cart_button(self):
        return self.webelement_by_xpath('//button/span[text()= "Add To Cart"]/..')

    def edit_button(self):
        return self.webelement_by_id('edit')

    def delete_button(self):
        return self.webelement_by_id('deleteButton')

    def one_star_button(self):
        return self.webelement_by_id('star_0')

    def two_stars_button(self):
        return self.webelement_by_id('star_1')

    def three_stars_button(self):
        return self.webelement_by_id('star_2')

    def four_stars_button(self):
        return self.webelement_by_id('star_3')

    def five_stars_button(self):
        return self.webelement_by_id('star_4')

    def rating_textarea(self):
        return self.webelement_by_id('mat-input-6')

    def save_rating_button(self):
        return self.webelement_by_xpath('//button/span[text()= "Save rating"]/..')
