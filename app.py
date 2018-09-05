import os

from flask import jsonify

from main import create_app

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)

@app.route('/')
def index():
    return jsonify(dict(message='Welcome to the Todo api'))


if __name__ == '__main__':
    app.run()
