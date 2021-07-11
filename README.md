## Setup

- Install Python3
- create a venv `python3 -m venv venv`
- activate the venv `. venv/bin/activate`
- to deactivate venv `deactivate`
- Install the dependencies `pip3 install -e .`
- Install chromedriver for feature testing `sbase install chromedriver`
- Run the app
  * `export FLASK_APP=acebook`
  * `flask run`

## Developing
- Add further dependencies to `setup.py`
- Then run this to install them `pip3 install -e .`
