# import required modules
import sqlite3

# click is used for accessing the command line interface
import click
from flask import current_app, g
from flask.cli import with_appcontext

# g is an object provided by flask - it is a global namespace for holding any data you want during a session. g is like 'global'
def get_db():
    # if there is no db currently in the global scope, connect to it
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            # some sort of conversion
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # returning dictionary rows (instead of tuples)
        g.db.row_factory = sqlite3.Row

    # if there is a databse in the global scope, return the database
    return g.db


def close_db(e=None):
    # removing the db from the global(?) list
    db = g.pop('db', None)

    if db is not None:
        db.close()

# set the db variable to the output of the get_db method.
def init_db():
    db = get_db()

    # run the schema.sql script to build the database
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

# use the click module to interact with the command line
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    # tells flask to run this command
    app.teardown_appcontext(close_db)
    # cli = command line interface
    app.cli.add_command(init_db_command)
