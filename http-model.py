#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import flask
from models import naive_bayes

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
    if request.method is not 'GET':
        nb = naive_bayes.HTTPNaiveBayesModel(name)
        model = nb.new_naive_bayes_model()
        naive_bayes.serialize_model(model, 'models/pickled_models/{}'.format(name))
        return 'The {0} model has been created. It can be updated here /model/{0}.\n'.format(name)
    else:
        return 'You can create a new model called {0} here!\n'.format(name)


if __name__ == '__main__':
    app.run(host='localhost', port=8909, debug=True)