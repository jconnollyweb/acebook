# importing modules: 'os' - provides a portable way of using operating system functionality
# 'flask' - the web development framework
import os
from acebook.auth import login_required
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# creating a method called create_app, test_config set to None by default
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # SECRET_KEY used to keep data safe
        SECRET_KEY='super_secret_key',
        # path where sqlite database will be saved
        DATABASE=os.path.join(app.instance_path, 'acebook.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # from the current folder, import the db file. Run the init_app method, this starts the connection to the database
    from . import db
    db.init_app(app)

    # from the current folder, import the auth file. Creating routes in app.
    from . import auth
    app.register_blueprint(auth.bp)

    # from the current folder, import the posts file. Creating routes in app.
    from . import posts
    app.register_blueprint(posts.bp)
    app.add_url_rule('/', endpoint='index')

    return app