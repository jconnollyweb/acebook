# Acebook Flask Template

_Coaching this? Find the source
[here.](https://github.com/makersacademy/slug/blob/main/materials/universe/acebook/seeds/python/README.ed.md)_

This template app was built using Python3, the Flask web framework and Pytest.

### Features
- Users can sign up, sign in and log out
- They can also create, read update and delete (CRUD) posts
- Users have to be signed in to create posts
- Users can only update or delete their own posts

### Design
- posts.py and auth.py are views (the equivalent of Sinatra controllers)
- post.py and user.py are models
- db.py looks after creating the database connection

## Quickstart

To run the server:

```shell
# If you haven't installed pipenv yet, install that first.
; pip3 install --user pipenv

# Install dependencies
; pipenv install

# Set up the database
; FLASK_APP=acebook pipenv run flask init-db

# Run the server
; FLASK_APP=acebook pipenv run flask run
```

To run the tests:

```shell
# Run the tests
# First, set up chromedriver — you'll only need to do this once.
; pipenv run sbase install chromedriver latest

# Then, run the server and keep it running.
; FLASK_APP=acebook pipenv run flask run
# Don't hit ctrl-C — keep it running!

# Finally, in another terminal window, run the tests
; pipenv run pytest
```

Pytest is very similar to `unittest`, but with a nicer display.

## Running the tests
- To run them all `pytest`
- To run the tests in a specific file, e.g. test_auth.py `pytest
  ./tests/test_auth.py`

## Dependency management

To add dependencies, run:

```shell
; pipenv install mydependency
```

## Altering the database

At some point in the not too distant future, you'll want to alter the database
in some way. E.g. By adding a new column to an existing table or by creating a
new table. The simplest way to do this is to edit `schema.sql`, then re-run
`flask init-db`. BUT... this will drop and recreate the existing tables and
you'll lose any data contained within them.


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/acebook-flask-template&prefill_File=README.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/acebook-flask-template&prefill_File=README.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/acebook-flask-template&prefill_File=README.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/acebook-flask-template&prefill_File=README.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy/acebook-flask-template&prefill_File=README.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->

# Acebook - Team Pandas
Team Members: John, Mathew, Lynsey, Abdul, Dan

This project is part of the Makers Apprentice Programming Course, and constitutes weeks 9 and 10 of the course. This project will take place over 2 weeks.


## Progress Log
Day 1:
- Discussed and set out ground rules for team working, eg. breaks, meeting frequency.
- Forked GitHub repo and invited team members to collaborate.
- Quick, high-level review of the existing codebase, including running the app in its current form.
- Copied existing Trello board, reviewed outstanding actions and populated it with new actions based on our agreed vision for the project.

Day 2:
- Moved calls over to Discord as Zoom was not meeting our needs for longer meetings.
- Created diagrams of current and envisioned project (see below).
- As a team, work through existing code and try to understand the syntax, modules and databases that we are unfamiliar with.
- Arranged our Trello board actions into groups in an attempt to minimise future merge conflicts.
- Created a shared vision of the MVP, discussed the small steps required to fulfill of our MVP actions, and tried to see where blockers may occur.

**MVP map**
![/MVP](https://imgur.com/vau1Sub)

**Posts page (/index)**
![/index](https://imgur.com/iUro8aA)

**New post page (/create)**
![/create](https://imgur.com/bkJv1af)
