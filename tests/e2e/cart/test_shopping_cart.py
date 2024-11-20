import pytest
import os
from tests.root import BASE_URL, USERNAME, PASSWORD
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# Este es el primer archivo de prueba en el Stream. Es el más básico y sencillo de todos.

class TestShoppingCart:
    
    def test_1_should_add_item_to_cart(seft, login: WebDriver):
        web = login
        products_to_add_cart = web.find_elements(By.CSS_SELECTOR, '[data-test^="add-to-cart"]')
        assert len(products_to_add_cart) > 0
        firstProduct = products_to_add_cart[0]
        firstProduct.click() # Product should be added to Shopping Cart
        
        web.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]').click()
        actual_url = web.current_url
        assert "cart" in actual_url 
        
        product_added_to_cart = web.find_elements(By.CSS_SELECTOR, '.cart_item')
        products_in_cart = len(product_added_to_cart)
        assert products_in_cart == 1 #? Product should be added to Shopping Cart
        

if __name__ == "__main__":
    pytest.main()