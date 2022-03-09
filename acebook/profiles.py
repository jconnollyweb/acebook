import os
from xml.etree.ElementTree import Comment
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from acebook.auth import login_required
from acebook.db import get_db

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/edit-profile')
@login_required
def edit_profile():
    bio = request.form['bio']
    file = request.files['file']

    