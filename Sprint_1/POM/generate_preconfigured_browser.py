from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def generate_preconfigured_browser():
    options = Options()
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    return browser