import os
from flask import Flask, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flask-orders-api.sqlite'),
            )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # ensure the instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page to display hello
    @app.route('/hello')
    def hello():
        response = {
                'message': 'Hello, World!',
                'status' : 'success'
                }
        return jsonify(response)

    from . import db
    db.init_app(app)

    from . import orders
    app.register_blueprint(orders.bp)

    return app
