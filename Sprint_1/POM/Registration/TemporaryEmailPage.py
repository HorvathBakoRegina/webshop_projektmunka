from Sprint_1.POM.GeneralPage import GeneralPage

class TemporaryEmailPageClass(GeneralPage):
    def __init__(self, browser):
        self.url = 'https://tempmailgenerator.co/'
        super().__init__(self.url, browser)

    def temporary_email(self):
        return self.webelement_by_id('mainEmail')

    def incoming_email(self):
        return self.webelement_by_id('mailbox')

    def activation_link(self):
        return self.webelement_by_xpath('//a[contains(@href, "/confirm")]')

    def iframe(self):
        return self.webelement_by_id('myContent')