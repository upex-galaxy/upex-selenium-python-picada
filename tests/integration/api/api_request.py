import requests
import os
from api.utils.file import save_json_to_file
from dotenv import load_dotenv
load_dotenv() 

class Api:
    
    def __init__(self):
        self.base_url = 'https://demoqa.com'
        self.access_token = None
        self.endpoints = {
            'create_user': '/Account/v1/User',
            'generate_token': '/Account/v1/GenerateToken',
            'get_collection': '/Account/v1/User/', # GET with path {userId}
            'store_books': '/BookStore/v1/Books', # GET
            'add_books': '/BookStore/v1/Books', # POST
            'delete_collection': '/BookStore/v1/Books', # DELETE
        }
        
    def save_response_json(self, data: object, file_name: str):
        save_json_to_file(json_data=data, dir_path='integration/res', file_name=file_name)
    
    def bearer_token(self):
        return {
            "Authorization": f"Bearer {self.access_token}"
        }
        
    def create_new_user(self, username, password):
        url = self.base_url + self.endpoints['create_user']
        request_data = {
            "userName": username,
            "password": password
        }
        response = requests.post(url, data=request_data)
        # assert response.status_code == 201
        body: object = response.json()
        self.save_response_json(data=body, file_name='create_new_user.json')
        return (body, response)
    
    def set_access_token(self):
        url = self.base_url + self.endpoints['generate_token']
        username = os.getenv('USERNAME')
        password = os.getenv('PASSWORD')
        request_data = {
            "userName": username,
            "password": password
        }
        response = requests.post(url, data=request_data)
        assert response.status_code == 200
        body: object = response.json()
        self.access_token: str = body['token']
        self.save_response_json(data=body, file_name='set_access_token.json')
        return (body, response)
    
    def get_store_books(self):
        url = self.base_url + self.endpoints['store_books']
        response = requests.get(url)
        assert response.status_code == 200
        body: object = response.json()
        self.save_response_json(data=body, file_name='get_store_books.json')
        return body
    
    def get_user_books_collection(self):
        url = self.base_url + self.endpoints['get_collection'] + os.getenv('USER_ID')
        response = requests.get(url, headers=self.bearer_token())
        assert response.status_code == 200
        body: object = response.json()
        self.save_response_json(data=body, file_name='get_user_books_collection.json')
        return body
    
    def delete_user_all_books(self):
        url = self.base_url + self.endpoints['delete_collection']
        query = {
            "UserId": os.getenv('USER_ID')
        }
        response = requests.delete(url, params=query, headers=self.bearer_token())
        assert response.status_code == 204 # No Content
        return response
        

    def add_books_to_collection(self, ids: list[object]):
        """
        Summary:
            Adds a list of books to the user's collection.

        Args:
            ids (list[object]): A list of objects, each containing an "isbn" property, representing the books to be added to the collection.

        Returns:
            tuple: A tuple containing the response body as an object and the response itself. The response body includes the user object with the "books" property, which contains the list of newly added books.
        """
        url = self.base_url + self.endpoints['add_books']
        request_data = {
            "userId": os.getenv('USER_ID'),
            "collectionOfIsbns": ids
        }
        response = requests.post(url, json=request_data, headers=self.bearer_token())
        # assert response.status_code == 201
        body: object = response.json()
        self.save_response_json(data=body, file_name='add_books_to_collection.json')

        return (body, response)