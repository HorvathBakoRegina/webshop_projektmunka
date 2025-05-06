from Sprint_1.POM.generate_preconfigured_browser import generate_preconfigured_browser

class GeneralPage(object):
    def __init__(self, url, browser=None):
        self.url = url
        if browser is None:
            self.browser = generate_preconfigured_browser()
        else:
            self.browser = browser

    def get(self):
        self.browser.get(self.url)

    def close(self):
        self.browser.close()

    def quit(self):
        self.browser.quit()

    def refresh(self):
        self.browser.refresh()

    def get_title(self):
        return self.browser.title

    def get_url(self):
        return self.browser.current_url
