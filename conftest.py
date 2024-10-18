# This File will be used soon in a future Stream to demonstrate how to use fixtures in Pytest
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOpt

@pytest.fixture
def web():
    options = ChromeOpt()
    options.add_argument("--headless")
    web = Chrome(options=options)
    return web