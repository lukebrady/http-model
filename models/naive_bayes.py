import pickle


from textblob.classifiers import NaiveBayesClassifier


# Create a new empty Naive Bayes model if it does not exist.
# @param name: The name of the new model. This must be unique.
def new_naive_bayes_model(name, data_set = None):
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
def serialize_model(model, path):
    # Dump the model to disk.
    try:
        pickle_file = open(path, mode='wb')
        pickle.dump(model, pickle_file)
    except IOError:
        return 'Error: Could not serialize the model to {}.'.format(path)