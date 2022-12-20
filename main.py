import requests
from pprint import pprint
from PyInquirer import prompt, print_json, Separator

def google_books_query():
	user_query = [{
		'type': 'input',
		'name': 'keyword',
		'message': "Enter a keyword to query the Google Books API:",
    }]
	user_answer = prompt(user_query)
	
	# URL for the Google Books API:
	api_url = "https://www.googleapis.com/books/v1/volumes"
	# Query parameters for the API request:
	params = {"q": user_answer["keyword"], "maxResults": 5}
	# Make a GET request to the API:
	try: 
		response = requests.get(api_url, params=params)
		# Early abort if status code not 200:
		if response.status_code != 200:
			print("An error occurred, please try later:", response.status_code)			
		data = response.json()		
		# Iterate through books and get author, title, and publisher:
		books = []
		for book in data["items"]:
			book = {
				"author": book["volumeInfo"]["authors"][0],
				"title": book["volumeInfo"]["title"],
				"publisher": book["volumeInfo"]["publisher"]
			}
			books.append(book)
		return books
		# pprint(books)
		# print(f"{title} by {author} - ({publisher})")
	except Exception as e:		
		print(f'Sorry, the Google Books API could not understand that query. Ensure that you only enter text. The error was found here: {e}')
# google_books_query()

def select_save_book():
	books = google_books_query()







