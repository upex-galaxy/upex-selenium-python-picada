from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from tests.e2e.pages.utils.locator import Locator

class ProductPage(Locator):
    
    def __init__(self, web: WebDriver, product: WebElement):
        super().__init__(web)
        self.product = product
        
        self.add_to_cart_button = lambda: self.product.find_element(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        self.product_price = lambda: float(self.product.find_element(By.CSS_SELECTOR, '.inventory_item_price').text.replace('$', ''))


    def add_to_cart(self):
        self.add_to_cart_button().click()