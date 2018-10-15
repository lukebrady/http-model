# Converts JSON into a data set that can be used by a classifier.
import json

def convert_json_into_data_set(json_obj):
    # Create an empty data set array.
    data_set = []
    # Convert the JSON object into a native python object.
    obj = json.loads(json_obj)
    # Now iterate through the created object and convert into a data set.
    for data in obj['Data']:
        data_set.append(tuple(data))
    # Now return the newly created data set.
    print(data_set)
    return data_set


if __name__ == '__main__':
    jsonString = open('test.json', 'r').read()
    convert_json_into_data_set(jsonString)