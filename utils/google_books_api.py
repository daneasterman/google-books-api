import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_books(query):
	GOOGLE_BOOKS_API_KEY = os.getenv('GOOGLE_BOOKS_API_KEY')
	params = {"q": query, "maxResults": 5, "key": GOOGLE_BOOKS_API_KEY}	
	API_URL = "https://www.googleapis.com/books/v1/volumes"	
	api = requests.get(API_URL, params=params)
	data = api.json()
	found_books = []
	for book in data["items"]:
			book = {
				"author": book["volumeInfo"]["authors"],
				"title": book["volumeInfo"]["title"],
				"publisher": book["volumeInfo"].get("publisher", "None")
			}
			found_books.append(book)
	if found_books:
		print("Your 5 books:")
		for book in found_books:
			print(f"Title: {book['title']}, Author: {book['author']}, Publisher: ({book['publisher']})")
	
	return found_books
