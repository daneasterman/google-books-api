import requests
from PyInquirer import prompt

READING_LIST = []

def google_books_query():
	question = [{
		'type': 'input',
		'name': 'keyword',
		'message': "Enter a keyword to query the Google Books API. Example: 'python'",
    }]
	answer = prompt(question)	
	# URL for the Google Books API:
	api_url = "https://www.googleapis.com/books/v1/volumes"
	# Query parameters for the API request:
	params = {"q": answer["keyword"], "maxResults": 5}
	# Make a GET request to the API:	
	response = requests.get(api_url, params=params)
	# Early abort if status code not 200:
	if response.status_code != 200:
		print("An error occurred, please try later:", response.status_code)			
	try:
		data = response.json()		
		books = []
		# Iterate through books and get author, title, and publisher:
		for book in data["items"]:
			book = {
				"author": book["volumeInfo"]["authors"][0],
				"name": book["volumeInfo"]["title"],
				"publisher": book["volumeInfo"]["publisher"]
			}
			books.append(book)
		return books		
	except Exception as e:		
		print(f'Sorry, the Google Books API could not understand that query. The error was found here: {e}')

def select_save_book():	
	api_books = google_books_query()
	print("Your 5 books:")
	for book in api_books:
		print(f"Title: {book['name']}, Author: {book['author']}, Publisher: ({book['publisher']})")	

	question = [{
				"type": "list",
        "message": "Please select a book you would like to save to your reading list by title:",
        "name": "books",
        "choices": api_books
				}]	
	answer = prompt(question)
	READING_LIST.append(answer)
	decide_next_steps()

def decide_next_steps():
	question = [{
					"type": "list",
					"message": "What would you like to do next?",
					"name": "next_steps",
					"choices": [
						"Save another book to your reading list",
						"View reading list",
						"Exit the program"
						]

					}]
	answer = prompt(question)
	if answer["next_steps"] == "Save another book to your reading list":
		select_save_book()
	elif answer["next_steps"] == "View reading list":
		print("Your reading list:")
		for b in READING_LIST:
			print(f" - {b['books']}")
		decide_next_steps()
	else:
		exit()
		
if __name__ == "__main__":
	select_save_book()