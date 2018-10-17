#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import flask
from flask import request

import model_json
import model_redis
from models import naive_bayes

# Create the flask server that will server the models.
app = flask.Flask(__name__)


# Create the index route.
@app.route('/', methods=['GET'])
def index():
    return 'Hello from the model server!'


# Create a new model that will server traffic and can be updated dynamically.
@app.route('/model/list', methods=['GET'])
def get_model():
    return 'This will be the list of created models.'


# Create a new model that will server traffic and can be updated dynamically.
@app.route('/model/<name>/create', methods=['POST'])
def create_model(name):
    json = request.json
    if json is not None:
        model = naive_bayes.new_naive_bayes_model(json)
        # Serialize the model to disk.
        model_redis.set_model(name, model)
        # naive_bayes.serialize_model(model, 'models/pickled_models/{}'.format(name))
        return 'The {0} model has been created. It can be updated here /model/{0}/update.\n'.format(name)
    else:
        return 'An initial data set must be submitted to create a model.'


# Update a created model.
@app.route('/model/<name>/update', methods=['POST'])
def update_model(name):
    # Now convert the JSON that was submitted in the request.
    data_set = model_json.convert_json_into_data_set(request.json)
    # Deserialize the model.
    # model = naive_bayes.deserialize_model('models/pickled_models/{}'.format(name))
    model = model_redis.get_model(name)
    # Update the model with the new data_set.
    model.update(data_set)
    print(model)
    # Re-serialize the model.
    # naive_bayes.serialize_model(model, 'models/pickled_models/{}'.format(name))
    model_redis.set_model(name, model)
    return 'The model has been successfully updated.\n'


# Classify a requests text.
@app.route('/model/<name>/classify', methods=['POST'])
def classify_request(name):
    # Deserialize the model.
    # model = naive_bayes.deserialize_model('models/pickled_models/{}'.format(name))
    model = model_redis.get_model(name)
    print(model)
    # Now convert the JSON that was submitted in the request.
    obj = request.json
    print(obj)
    classification = model.classify(obj['Text'])
    return '{}\n'.format(classification)


# Delete a model in the redis cache.
@app.route('/model/<name>/delete', methods=['GET'])
def delete_model(name):
    # Remove the model from redis.
    result = model_redis.remove_model(name)
    if int(result) != 1:
        return '{} could not be deleted.\n'.format(name)
    else:
        return '{} was successfully deleted.\n'.format(name)

if __name__ == '__main__':
    app.run(host='localhost', port=8909, debug=True)
