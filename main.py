import pynput
from PyInquirer import prompt
from requests import ConnectionError
from utils.google_books_api import get_books

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
		'name': 'search',
		'message': "Enter a keyword to query the Google Books API. Example: 'python'",
    }]
	answer = prompt(question)	
	try:
		if answer["search"]:
			found_books = get_books(answer)
			select_and_save(found_books)
		else:
			print("**Alert**: Please make sure that you enter a keyword")
			search_books()
	except ConnectionError:
			print("It appears that you are not connected to the internet. Please check your internet connection and restart the program.")
	except KeyError:
		print("Sorry, the API couldn't find anything with that keyword, please try again:")
		search_books()

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
	mouse_listener = pynput.mouse.Listener(suppress=True)
	mouse_listener.start()
	decide_action()	
		
if __name__ == "__main__":	
	main()
	