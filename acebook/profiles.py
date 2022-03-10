# importing a bunch of modules again
import functools
from acebook.auth import login_required
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
# modules for security
from werkzeug.security import check_password_hash, generate_password_hash

# making the get_db method accessible from the db file, and the User class accessible from the user file
from acebook.db import get_db
from acebook.user import User

# create a variable called bp, containing a Blueprint. __name__ assigning profile as the name?
bp = Blueprint('profile', __name__, url_prefix='/profile')

@bp.route('/view', methods=('GET', 'POST'))
@login_required

def view():
    return render_template('profile/view.html')

@bp.route('/edit', methods=('GET', 'POST'))
@login_required
def edit():
  return render_template('profile/edit.html')

# # 'Such a function is executed before each request, even if outside of a blueprint.' Will check for user_id before a request is completed
# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')

#     if user_id is None:
#         # g.user confirms that information is part of the current session. 
#         # g is an object provided by flask - it is a global namespace for holding any data you want during a session
#         g.user = None
#     else:
#         g.user = User.find_by_id(user_id)


# @bp.route('/logout')
# def logout():
#     # clear the current session; forget who is logged in
#     session.clear()
#     return redirect(url_for('index'))

# # 
# def edit_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('profile.edit'))

#         return view(**kwargs)

#     return wrapped_view
