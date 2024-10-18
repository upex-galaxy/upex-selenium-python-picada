import os
from dotenv import load_dotenv
load_dotenv()

def get_tests_root():
    project_root = os.path.dirname(__file__)
    return project_root

USERNAME = os.getenv('SWL_USERNAME')
PASSWORD = os.getenv('SWL_PASSWORD')
TEST_ENV = os.getenv('TEST_ENV') ## ejemplo: qa, dev, prod

baseUrl = {
    'DEV': 'https://www.saucedemo.com/',
    'QA': 'https://www.saucedemo.com/',
    'PROD': 'https://www.saucedemo.com/'
}
BASE_URL = baseUrl[TEST_ENV]