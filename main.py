from utils.google_books_api import create_books_api
from PyInquirer import prompt

READING_LIST = []

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
	# print("The program has now ended, goodbye")	
		
if __name__ == "__main__":
	decide_action()