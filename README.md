# Acebook Flask Template

This template app was built using Python3, the Flask microframework and pytest.

### Features
- Users can sign up, sign in and log out
- They can also create, read update and delete (CRUD) posts
- Users have to be signed in to create posts
- Users can only update or delete their own posts

### Design
- posts.py and auth.py are views (the equivalent of Sinatra controllers)
- post.py and user.py are models
- db.py looks after creating the database connection

## Setup
- Install Python3
- Create a virtual environment `python3 -m venv venv`
- Activate the virtual environment `. venv/bin/activate`
- Install the dependencies `pip3 install -e .`
- Install chromedriver for feature testing `sbase install chromedriver`
- Create and migrate the database
  * `export FLASK_APP=acebook`
  * `flask init-db`
- Run the app
  * `flask run`

## Running the tests
- To run them all `pytest`
- To run the tests in a specific file, e.g. test_auth.py `pytest ./tests/test_auth.py`
## Dependency management
- Add further dependencies to `setup.py`
- Then run this to install them `pip3 install -e .`
