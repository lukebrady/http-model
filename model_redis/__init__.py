import redis
import pickle

r = redis.StrictRedis(port=6381)

def set_model(name, model):
    pickle_model = pickle.dumps(model)
    # Use the globally accessible redis object to cache model.
    r.set(name, pickle_model)

def get_model(name):
    pickle_model = r.get(name)
    if pickle_model is not None:
        # Unpickle the model and return.
        return pickle.loads(pickle_model)
    return 'The {0} model does not exist.\nYou can create it using /model/{0}/create.\n'.format(name)

def remove_model(name):
    result = r.delete(name)
    return result



