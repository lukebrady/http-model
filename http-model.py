#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import flask

from flask import request, redirect

# Create the flask server that will server the models.
app = flask.Flask(__name__)

# Create the index route.
@app.route('/', methods=['GET'])
def index():
    return 'Hello from the model server!'

# Create a new model that will server traffic and can be updated dynamically.
@app.route('/model', methods=['GET'])
def get_model():
    return 'This will be the list of created models.'

# Create a new model that will server traffic and can be updated dynamically.
@app.route('/model/<name>', methods=['GET', 'POST'])
def create_model(name):
    print(name)
    return 'You can create a new model called {0} here!'.format(name)


if __name__ == '__main__':
    app.run(host='localhost', port=8909, debug=True)