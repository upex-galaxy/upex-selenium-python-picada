import pytest
import os
from tests.root import BASE_URL, USERNAME, PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# Este es el primer archivo de prueba en el Stream. Es el más básico y sencillo de todos.

class TestShoppingCart:
    
    @pytest.fixture
    def driver(self, web: WebDriver):
        web.implicitly_wait(10)
        web.get(BASE_URL)
        print(f"User: {USERNAME}")
        web.find_element(By.CSS_SELECTOR, '[data-test=username]').send_keys(USERNAME)
        web.find_element(By.CSS_SELECTOR, '[data-test=password]').send_keys(PASSWORD)
        web.find_element(By.CSS_SELECTOR, '[data-test=login-button]').click()
        inventory_page = web.find_element(By.CSS_SELECTOR, '.inventory_list')
        assert inventory_page.is_displayed() == True
        yield web
    
    def test_1_should_add_item_to_cart(seft, driver: WebDriver):
        products_to_add_cart = driver.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        assert len(products_to_add_cart) > 0
        firstProduct = products_to_add_cart[0]
        firstProduct.click() # Product should be added to Shopping Cart
        
        driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        actual_url = driver.current_url
        assert "cart" in actual_url 
        
        product_added_to_cart = driver.find_elements(By.CSS_SELECTOR, '.cart_item')
        products_in_cart = len(product_added_to_cart)
        assert products_in_cart == 1 #? Product should be added to Shopping Cart
        

if __name__ == "__main__":
    pytest.main()