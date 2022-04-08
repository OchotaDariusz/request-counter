# Request counter

## Story

This assignment is a list of exercises for practicing Flask.
You can find multiple features which you can use separately after the Preparation part.
Do not forget to commit after you completed a part.

## What are you going to learn?

- Send HTTP requests with GET, POST, PUT and DELETE method.
- Use global variables with Flask and display their value on a page.
- Write different behaviors for different HTTP methods on the same endpoint.

## Tasks

1. Initialize an empty Flask project with a new virtualenv and a `.gitignore` file.
    - A `venv` folder containing a virtual environment with at least python 3.8 is created.
    - A `requirements.txt` with Flask as one of the requirements is created.
    - A `templates` folder is created for your HTML template files.
    - A `server.py` is created, in which you can handle incoming HTTP requests.
    - A `.gitignore` file is created to ignore unnecessary venv, pyCharm, Flask, or python files.

2. Create a `/` route for the main page from which users can reach the features of the Request counter.
    - The page has a GET-Request link that sends a GET request to the `/request-counter` route
    - The page has a POST-Request button (in a form) that sends a POST request to the `/request-counter` route
    - The page has a Statistics link that navigates to the `/statistics` route

3. Create a `/request-counter` route that can count incoming HTTP requests.
    - The numbers of requests are stored for each HTTP method (GET, POST, DELETE, PUT) in separate global variables.
    - After increasing the count this route redirects to main page.

4. Create a `/statistics` route which can show the count results.
    - The page has a link which leads back to to home page.
    - The page has a table which contains 4 rows (one for each HTTP method) and two columns (one for the method name and one for the request count).

5. Store the request count data in a text file instead of global variable.
    - A text file named `request_counts.txt` is created.
    - The `request_counts.txt`'s content is the following.
GET: 5
POST: 3
DELETE: 1
PUT: 0

## General requirements

None

## Hints

- You can send PUT and DELETE requests with Curl. This way you can try your request counter with all HTTP methods to make sure it works.

## Background materials

- <i class="far fa-exclamation"></i> [Pip and VirtualEnv](project/curriculum/materials/pages/python/pip-and-virtualenv.md)
- <i class="far fa-exclamation"></i> [A web-framework for Python: Flask](project/curriculum/materials/pages/python/python-flask.md)
- <i class="far fa-book-open"></i> [Flask documentation](http://flask.palletsprojects.com/) (the Quickstart gives a good overview)
- <i class="far fa-book-open"></i> [Install Curl](https://www.howtoinstall.co/en/ubuntu/xenial/curl)
- <i class="far fa-book-open"></i> [Example to test DELETE/PUT request](https://www.garron.me/en/bits/curl-delete-request.html)
- <i class="far fa-book-open"></i> [Ports](project/curriculum/materials/pages/networks/ports.md)
