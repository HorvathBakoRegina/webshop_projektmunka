from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class GeneralPage(object):
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 60)

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

    def swich_to(self):
        return self.browser.switch

    def webelement_by_xpath(self, xpath):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, f'{xpath}')))

    def webelement_by_id(self, id):
        return self.wait.until(EC.element_to_be_clickable((By.ID, f'{id}')))

    def webelements_by_id(self, id):
        return self.wait.until(EC.visibility_of_all_elements_located((By.ID, f'{id}')))

