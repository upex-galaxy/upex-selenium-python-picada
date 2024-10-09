import os
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from tests.e2e.pages.utils.locator import Locator
from tests.root import get_tests_root

class ChatPpfPage(Locator):
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.file_uploader = lambda: self.web.find_element(By.ID, '__picker-input')
        self.loader = lambda: self.get_element_by_text('Analyzing with AI')
        self.chat_input = lambda: self.web.find_element(By.CSS_SELECTOR, 'form input[type=text]')
        self.chat_submit = lambda: self.web.find_element(By.CSS_SELECTOR, 'button[type=submit]')
        self.chat_answers = lambda: self.web.find_elements(By.CSS_SELECTOR, '[type=answer]') 
        self.chat_questions = lambda: self.web.find_elements(By.CSS_SELECTOR, 'div[type=question]')
        
    def upload_pdf(self, file_name: str):
        file_dir = os.path.join(get_tests_root(), 'data', file_name)
        self.file_uploader().send_keys(file_dir)
        
    def should_question_be_displayed(self, question: str):
        questions = self.chat_questions()
        last_question = questions[-1]
        assert last_question.text == question

    def get_last_ai_answer(self):
        self.wait_until_list_element_is_displayed('[type=answer]')
        last_answer = self.chat_answers()[-1]
        print(last_answer.text)
        return last_answer.text
        
    def chat_ai(self, question: str):
        self.chat_input().send_keys(question)
        # self.chat_submit().click()
        self.press_enter()
        self.should_question_be_displayed(question)
        