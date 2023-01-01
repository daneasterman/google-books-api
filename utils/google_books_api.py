import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_books(query):
	GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')
	params = {"q": f"{query}intitle:", "maxResults": 5, "key": GOOGLE_BOOKS_API_KEY}	
	API_URL = "https://www.googleapis.com/books/v1/volumes"	
	api = requests.get(API_URL, params=params)
	data = api.json()
	found_books = []
	for book in data["items"]:
		authors = book["volumeInfo"].get("authors")
		if not authors:
			pass
		else:
			book = {
				"author": book["volumeInfo"]["authors"],
				"name": book["volumeInfo"]["title"],
				"publisher": book["volumeInfo"]["publisher"]
			}
			found_books.append(book)
	if found_books:
		print("Your 5 books:")
		for book in found_books:
			print(f"Title: {book['name']}, Author: {book['author']}, Publisher: ({book['publisher']})")
	
	return found_books
