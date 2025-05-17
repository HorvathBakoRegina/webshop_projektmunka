from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


class GeneralPageClass(object):
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 5)

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

    def visibility_of_webelement_by_xpath(self, xpath):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, f'{xpath}')))

    def webelement_by_id(self, id):
        return self.wait.until(EC.element_to_be_clickable((By.ID, f'{id}')))

    def visibility_of_webelement_by_id(self, id):
        return self.wait.until(EC.visibility_of_element_located((By.ID, f'{id}')))

    def webelements_by_id(self, id):
        return self.wait.until(EC.visibility_of_all_elements_located((By.ID, f'{id}')))

    def webelements_by_xpath(self, xpath):
        return self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, f'{xpath}')))

    def webelement_by_classname(self, classname):
        return self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, f'{classname}')))

    def visibility_of_webelement_by_classname(self, classname):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, f'{classname}')))

    def webelements_by_classname(self, classname):
        return self.browser.find_elements(By.CLASS_NAME, classname)

    def webelement_by_formcontrolname(self, formcontrolname):
        xpath = f'//input[@formcontrolname="{formcontrolname}"]'
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, f'{xpath}')))

    def error_message(self, element):
        attribute = element.get_attribute("aria-describedby")
        return self.webelement_by_id(f'{attribute}')



