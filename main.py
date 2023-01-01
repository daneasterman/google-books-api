# from pynput import mouse
# import mouse
from PyInquirer import prompt
from requests import ConnectionError
from utils.google_books_api import create_books_api

READING_LIST = []

def clicking_alert():
	print("Sorry, using the mouse is not supported in this application. Please try running the program again.")	

def goodbye():
	print("Thank you for using the Google Books CLI.")

def decide_action():	
	question = [{
					"type": "list",
					"message": "Main Menu: Google Books CLI. What would you like to do?",
					"name": "action",
					"choices": ["Search for a book", "View your reading list", "Exit the program"]
					}]
	try:
		answer = prompt(question)
		if answer.get("action") == "Search for a book":
		# if answer["action"] == "Search for a book":
			search_books()
		elif answer.get("action") == "View your reading list":
			if READING_LIST:
				print("Your reading list:")
				for b in READING_LIST:
					print(f" - {b['books']}")
				decide_action()
			else:
				print("No books saved to reading list yet.")
				decide_action()
		# elif answer.get("action") == "Exit the program":
		else:
			exit()
	except EOFError:
		print("The CLI was terminated by the user with CTRL+D")

def search_books():
	question = [{
		'type': 'input',
		'name': 'keyword',
		'message': "Enter a keyword to query the Google Books API. Example: 'python'",
    }]
	answer = prompt(question)		
	if answer:
		try: 
			api = create_books_api(answer)		
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
				select_and_save(found_books)
		except ConnectionError:
			print("It appears that you are not connected to the internet. Please check your internet connection and try again.")

def select_and_save(books):	
	question = [{
				"type": "list",
        "message": "Please select a book you would like to save to your reading list by title:",
        "name": "books",
        "choices": books
				}]
	answer = prompt(question)	
	READING_LIST.append(answer)
	decide_action()


def main():	
	decide_action()
		
if __name__ == "__main__":
	main()
	