from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class MyCartPage:
    def __init__(self, browser):
        self.browser = browser

    def open_cart(self):
        return self.browser.find_element(By.ID, "button_myCart").click()

    def continue_shopping(self):
        return self.browser.find_element(By.XPATH, "//span[text()='Continue shopping']").clikc()

    def remove_item(self):
        minus_button = self.browser.find_elements(By.XPATH, "//button[contains(@class, 'minus_button')]") # itt indexelni kell mert több ilyen gomb van
        minus_button.click()
        x_button = self.browser.find_element(By.XPATH, "//mat-icon[text()='close']") # itt indexelni kell mert több ilyen gomb van
        x_button.click()

    def click_checkout(self):
        self.browser.find_element(By.XPATH, "//span[text()='Check out']").click()
