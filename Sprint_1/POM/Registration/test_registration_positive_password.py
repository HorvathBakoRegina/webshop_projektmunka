from Sprint_1.POM.Pages.RegistrationPage import RegistrationPageClass
from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

class TestTC(object):
    def setup_method(self):
        self.browser = generate_preconfigured_browser()
        self.pageRegistration = RegistrationPageClass(self.browser)
        self.pageRegistration.get()

        self.green1 = 'mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color green'
        self.green2 = 'mat-icon notranslate material-icons mat-ligature-font green mat-icon-no-color'
        self.black1 = 'mat-icon notranslate material-icons mat-ligature-font mat-icon-no-color black'
        self.black2 = 'mat-icon notranslate material-icons mat-ligature-font black mat-icon-no-color'

    def teardown_method(self):
       self.pageRegistration.quit()

    def test_password_check_1(self):
        self.pageRegistration.input_password_first().send_keys('Teszt123')

        special_check = self.pageRegistration.password_check_special().get_attribute('class')
        capital_check = self.pageRegistration.password_check_capital().get_attribute('class')
        number_check = self.pageRegistration.password_check_number().get_attribute('class')
        length_check = self.pageRegistration.password_check_length().get_attribute('class')

        assert special_check in [self.black1, self.black2]
        assert capital_check in [self.green1, self.green2]
        assert number_check in [self.green1, self.green2]
        assert length_check in [self.green1, self.green2]

    def test_password_check_2(self):
        self.pageRegistration.input_password_first().send_keys('teszt123!')

        special_check = self.pageRegistration.password_check_special().get_attribute('class')
        capital_check = self.pageRegistration.password_check_capital().get_attribute('class')
        number_check = self.pageRegistration.password_check_number().get_attribute('class')
        length_check = self.pageRegistration.password_check_length().get_attribute('class')

        assert special_check in [self.green1, self.green2]
        assert capital_check in [self.black1, self.black2]
        assert number_check in [self.green1, self.green2]
        assert length_check in [self.green1, self.green2]

    def test_password_check_3(self):
        self.pageRegistration.input_password_first().send_keys('Tesztteszt!')

        special_check = self.pageRegistration.password_check_special().get_attribute('class')
        capital_check = self.pageRegistration.password_check_capital().get_attribute('class')
        number_check = self.pageRegistration.password_check_number().get_attribute('class')
        length_check = self.pageRegistration.password_check_length().get_attribute('class')

        assert special_check in [self.green1, self.green2]
        assert capital_check in [self.green1, self.green2]
        assert number_check in [self.black1, self.black2]
        assert length_check in [self.green1, self.green2]

    def test_password_check_4(self):
        self.pageRegistration.input_password_first().send_keys('Tes1!')

        special_check = self.pageRegistration.password_check_special().get_attribute('class')
        capital_check = self.pageRegistration.password_check_capital().get_attribute('class')
        number_check = self.pageRegistration.password_check_number().get_attribute('class')
        length_check = self.pageRegistration.password_check_length().get_attribute('class')

        assert special_check in [self.green1, self.green2]
        assert capital_check in [self.green1, self.green2]
        assert number_check in [self.green1, self.green2]
        assert length_check in [self.black1, self.black2]

    def test_password_check_5(self):
        self.pageRegistration.input_password_first().send_keys('teszt')

        special_check = self.pageRegistration.password_check_special().get_attribute('class')
        capital_check = self.pageRegistration.password_check_capital().get_attribute('class')
        number_check = self.pageRegistration.password_check_number().get_attribute('class')
        length_check = self.pageRegistration.password_check_length().get_attribute('class')

        assert special_check in [self.black1, self.black2]
        assert capital_check in [self.black1, self.black2]
        assert number_check in [self.black1, self.black2]
        assert length_check in [self.black1, self.black2]

    def test_password_check_6(self):
        self.pageRegistration.input_password_first().send_keys('Ékezet1%')

        special_check = self.pageRegistration.password_check_special().get_attribute('class')
        capital_check = self.pageRegistration.password_check_capital().get_attribute('class')
        number_check = self.pageRegistration.password_check_number().get_attribute('class')
        length_check = self.pageRegistration.password_check_length().get_attribute('class')

        assert special_check in [self.green1, self.green2]
        assert capital_check in [self.green1, self.green2]
        assert number_check in [self.green1, self.green2]
        assert length_check in [self.green1, self.green2]
