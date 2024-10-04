import random
import pytest
from api.api_request import Api

class TestBooksApi:
    
    def test_should_authenticate(self):
        api = Api()
        [json, res] = api.set_access_token()
        assert res.status_code == 200
        assert json['token'] != None
        print(json)
        
    def test_should_add_book_to_collection(self):
        api = Api()
        api.set_access_token()
        prev_user_collection = api.get_user_books_collection()
        if prev_user_collection['books'] != []:
            print("Deleting all books from collection")
            api.delete_user_all_books()
            collection = api.get_user_books_collection()
            assert collection['books'] == []
        
        # Get a random book from the store
        body = api.get_store_books()
        available_books = len(body['books'])
        random_book = random.randint(0, available_books)
        book_id = body['books'][random_book]['isbn']
        assert book_id != None
        print(f"Random book selected: {book_id}")
        
        # Add the book to the collection
        data = [{"isbn": book_id}]
        [body, res] = api.add_books_to_collection(ids=data)
        assert res.status_code == 201
        assert body['books'] == data
        assert body['books'][0]['isbn'] == book_id
        
        # Check if the book is added in the collection
        user_collection = api.get_user_books_collection()
        actual_collection = user_collection['books']
        is_added = any(book['isbn'] == book_id for book in actual_collection)
        assert is_added == True


if __name__ == "__main__":
    pytest.main()