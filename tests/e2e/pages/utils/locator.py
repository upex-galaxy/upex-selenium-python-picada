from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait


class Locator:
    def __init__(self, driver: WebDriver):
        self.web = driver
        
    def get_element_by_text(self, text: str):
        xpath = f'//*[contains(text(), "{text}")]'
        element = self.web.find_element(By.XPATH, xpath)
        return element
    
    def get_element_by_matching_text(self, text: str):
        xpath = f'//*[text() = "{text}"]'
        element = self.web.find_element(By.XPATH, xpath)
        return element
    
    def press_enter(self):
        ActionChains(self.web).send_keys(Keys.ENTER).perform()

    def wait_until_list_element_is_displayed(self, locator: str, timeout=10):
        WebDriverWait(self.web, timeout).until(lambda web: web.find_elements(By.CSS_SELECTOR, locator)[0].is_displayed())