#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import flask
import model_json
from models import naive_bayes

from flask import request, redirect

# Create the flask server that will server the models.
app = flask.Flask(__name__)

model_cache = {}

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
    if request.method is not 'GET':
        nb = naive_bayes.HTTPNaiveBayesModel(name)
        model = nb.new_naive_bayes_model()
        # Add model to the model cache.
        model_cache[name] = model
        # Serialize the model to disk.
        naive_bayes.serialize_model(model, 'models/pickled_models/{}'.format(name))
        return 'The {0} model has been created. It can be updated here /model/{0}.\n'.format(name)
    else:
        return 'You can create a new model called {0} here!\n'.format(name)

# Update a created model.
@app.route('/model/<name>/update', methods = ['POST'])
def update_model(name):
    if model_cache.get(name) != None:
        model = model_cache.get(name)
        # Now convert the JSON that was submitted in the request.
        data_set = model_json.convert_json_into_data_set(request.data)
        # Update the model with the new data_set.
        model.update(data_set)
    return 'The model has been successfully updated.\n'

# Classify a requests text.
@app.route('/model/<name>/classify', methods=['POST'])
def classify_request(name):
    if model_cache.get(name) is not None:
        model = model_cache.get(name)
        # Now convert the JSON that was submitted in the request.
        print(request.data)
        classification = model.classify(request.data)
        return 'The data sent was classified as {}.\n'.format(classification)
    else:
        return 'Could not find the requested model.\n'


if __name__ == '__main__':
    app.run(host='localhost', port=8909, debug=True)