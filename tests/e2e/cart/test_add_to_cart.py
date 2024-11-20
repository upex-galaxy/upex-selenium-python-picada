import pytest
import random
from tests.e2e.pages.product_page import ProductPage
from tests.e2e.pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class TestAddToCart:
   
    #* ---- Test Cases ----:
    def test_GX3_5723_TC1_should_add_product_to_cart(self, login: WebDriver):
        """GX3-5723 TC1: Should add one product to cart and verify it is there."""
        web = login
        given_products = web.find_elements(By.CSS_SELECTOR, '[data-test="inventory-item"]')
        # choose a random product:
        random_index = random.randint(0, len(given_products) - 1)
        given_product = given_products[random_index]
        
        product = ProductPage(web, given_product)
        expected_price = product.product_price()
        product.add_to_cart()
        
        cart_page = ShoppingCartPage(web)
        assert cart_page.shopping_cart_counter() == 1
        
        cart_page.go_to_shopping_cart()
        assert cart_page.get_items_in_cart() == 1
        
        products_in_cart = cart_page.products_in_cart()
        product_in_cart = ProductPage(web, products_in_cart[0])
        assert product_in_cart.product_price() == expected_price

if __name__ == "__main__":
    pytest.main()