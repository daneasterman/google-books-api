## Google Books API Command Line Application

1. Install all dependencies from requirements file: `pip install -r requirements.txt`

2. Run project with: `python main.py`

### Workings / Brainstorming:

Below are some quick workings I used to confirm in my mind how I would structure the application before starting the actual coding.
After reading through the instructions, I distilled the task into 3 core requirements, so I decided the simplest way to think about it would be to create 3 core functions.
In the end it made sense for me to create a separate `decide_next_steps` function with its own distinct question / answer set rather than a separate `retrieve_reading_list` function as included in my initial brainstorming:

![IMG_9148](https://user-images.githubusercontent.com/4712052/208736594-722d474b-19d2-463a-bb71-a64483b72a15.jpg)

### New for Version 2:

Updated the Google Books API query to include an API key as stated in the official documentation. You can find instructions to add your API key here: [https://developers.google.com/books/docs/v1/using](https://developers.google.com/books/docs/v1/using)
Just create a `.env` file in the root of the project and add your key with this variable name: `GOOGLE_BOOKS_API_KEY`
