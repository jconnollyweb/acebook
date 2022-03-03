# importing a bunch of modules again
import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# modules for security
from werkzeug.security import check_password_hash, generate_password_hash

# making the get_db method accessible from the db file, and the User class accessible from the user file
from acebook.db import get_db
from acebook.user import User

# create a variable called bp, containing a Blueprint. __name__ assigning auth as the name?
bp = Blueprint('auth', __name__, url_prefix='/auth')

# connect to the /register route, 
@bp.route('/register', methods=('GET', 'POST'))
# define a register method
def register():
    # if POST request: accept the form input and set to username and password variables
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # to start with, set error to None
        error = None

        # if no username given in input form, set error message
        if not username:
            error = 'Username is required.'
        # if no password given in input form, set error message
        elif not password:
            error = 'Password is required.'
        # if username already exists (User class can find the username in database), set error message
        elif User.find(username) is not None:
            error = f"User {username} is already registered."

        # if there is no error found, create a new User class with the given username and password, then redirect to auth/login
        if error is None:
            User.create(username, password)
            session.clear()
            user = User.find(username) 
            session['user_id'] = user.id
            return redirect(url_for('profile'))
              
            
            # this can be altered to redirect to a different route - use of sessions to log in after registering?

        # if there is an error, flash it on the front end 
        flash(error)

    # if GET request: return the blank 'register' template
    return render_template('auth/register.html')

# similar to register route and logic above
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        error = None
        # Use the find method from the User class to set the username to the user variable
        user = User.find(username)

        if user is None:
            error = 'Incorrect username.'
        elif not user.authenticate(password):
            error = 'Incorrect password.'

        if error is None:
            # clear current session
            session.clear()
            # for this session, store the user.id and allow this to be used throughout this session
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')

# 'Such a function is executed before each request, even if outside of a blueprint.' Will check for user_id before a request is completed
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        # g.user confirms that information is part of the current session. 
        # g is an object provided by flask - it is a global namespace for holding any data you want during a session
        g.user = None
    else:
        g.user = User.find_by_id(user_id)


@bp.route('/logout')
def logout():
    # clear the current session; forget who is logged in
    session.clear()
    return redirect(url_for('index'))

# 
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view