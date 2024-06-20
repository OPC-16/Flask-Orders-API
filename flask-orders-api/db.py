import random
import sqlite3
import click
from flask import current_app, g, jsonify

# get_db() returns a database connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
                )
        g.db.row_factory = sqlite3.Row

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close();

def init_db():
    db = get_db()
    
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf-8'))

# a helper method to create few items
def create_items():
    db = get_db()
    for i in range(3):
        itemID = str(random.randint(1, 100))
        qty = str(random.randint(1, 50))
        price = str(random.randint(1, 1000))
        try:
            db.execute(
                    'INSERT INTO `item` (ItemID, OrderID, Quantity, Price) VALUES (?, ?, ?, ?)',
                    (itemID, i + 1, qty, price)
                    )
            db.commit()
        except sqlite3.IntegrityError:
            print('error occured while inserting item data')

    print('Items inserted successfully')

# click.command() defines a command-line command called 'init-db' which calls the init_db() method and shows a success message to the user on the terminal
@click.command('init-db')
def init_db_command():
    init_db()
    create_items()
    click.echo("Initialized the database.")

# The close_db() and init_db_command() functions need to be registered with the application instance; otherwise, they won’t be used by the application. However, since 
# we've used a factory function, that instance isn’t available when writing the functions. Instead, write a function that takes an application and does the 
# registration.
def init_app(app):
    app.teardown_appcontext(close_db)   # tells Flask to call that function when cleaning up after returning the response.
    app.cli.add_command(init_db_command)  # adds a new command that can be called with the 'flask' command, just like 'run' we can now use 'init-db'
