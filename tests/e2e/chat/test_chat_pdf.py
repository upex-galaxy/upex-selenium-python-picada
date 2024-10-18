import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.e2e.pages.pdf_upload_page import ChatPpfPage


class TestChatPDF:
    
    def test_should_chat_with_pdf(self, web: WebDriver):
        chat_pdf_page = ChatPpfPage(web)
        web.implicitly_wait(10)
        web.maximize_window()
        web.get('https://smallpdf.com/chat-pdf')

        file_name = 'upexgalaxy_lobby.pdf'

        chat_pdf_page.upload_pdf(file_name)
        while chat_pdf_page.loader().is_displayed() == True:
            pass
        chat_pdf_page.get_last_ai_answer()
        
        chat_pdf_page.chat_ai('What is the UPEX service that provides a Workspace to gain experience?')
        
        chat_pdf_page.get_last_ai_answer()
        
        pass
        
    
    

if __name__ == "__main__":
    pytest.main()

