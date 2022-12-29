import requests

def create_books_api(query):
	params = {"q": query, "maxResults": 5}
	API_URL = "https://www.googleapis.com/books/v1/volumes"
	api = requests.get(API_URL, params=params)
	if api.status_code != 200:
		print("An error occurred, please try later:", api.status_code)
	return api