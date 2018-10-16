import pickle
from os import path

from textblob.classifiers import NaiveBayesClassifier


class HTTPNaiveBayesModel:
    def __init__(self, name):
        self.name = name

    # Create a new empty Naive Bayes model if it does not exist.
    # @param name: The name of the new model. This must be unique.
    def new_naive_bayes_model(self, data_set = None):
        # Empty data_set if data set is supplied to the model.
        if data_set is None:
            data_set = [('test','test')]
            model = NaiveBayesClassifier(data_set)
        else:
            model = data_set
        # Now return the model.
        return model



# Serialize the model to disk that can be read into memory when needed.
# @param model: The model that will be serialized to disk.
# @param path: The location of the where the model will be serialized.
def serialize_model(model, model_path):
    if not path.exists(model_path):
        # Dump the model to disk.
        try:
            with open(model_path, mode='wb') as pickle_file:
                pickle.dump(model, pickle_file)
        except IOError:
            return 'Error: Could not serialize the model to {}.'.format(path)
    else:
        return '{} already exists.'.format(model)


# Serialize the model to disk that can be read into memory when needed.
# @param model: The model that will be serialized to disk.
# @param path: The location of the where the model will be serialized.
def deserialize_model(model_path):
    if path.exists(model_path):
        # Dump the model to disk.
        try:
            with open(model_path, mode='rb') as pickle_file:
                model = pickle.loads(pickle_file.read())
                return model
        except IOError:
            return 'Error: Could not serialize the model to {}.'.format(path)
    else:
        return '{} does not exist.'.format(model_path)