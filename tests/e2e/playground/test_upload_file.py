import pytest
import os
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from tests.root import get_tests_root

class TestFileUpload:
    
    def test_should_upload_file(self):
        web = Chrome()
        web.implicitly_wait(10)
        web.get('https://qaplayground.dev/apps/upload/')
        #* -----

        num_of_files_label = web.find_element(By.ID, 'num-of-files')
        file_upload_state = num_of_files_label.text
        assert file_upload_state == 'No File Selected'
        
        #* Read File to upload file...
        given_file_name = 'upercito.png'
        
        file_uploader = web.find_element(By.ID, 'file-input')
        file_dir = os.path.join(get_tests_root(), 'data', given_file_name)
        
        file_uploader.send_keys(file_dir)

        new_uploaded_state = num_of_files_label.text
        assert new_uploaded_state == '1 File Selected'
        
        image_exists = web.find_element(By.CSS_SELECTOR, 'img').is_displayed()
        assert image_exists == True
        
        file_name_locator = f'//*[contains(text(), {given_file_name})]'
        file_name_element = web.find_element(By.XPATH, file_name_locator)
        assert file_name_element.is_displayed() == True
        
        
        
        

        

if __name__ == "__main__":
    pytest.main()