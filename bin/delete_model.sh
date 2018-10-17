#!/usr/bin/env bash

# This script is used to delete an existing model.

if [[ -z $1 ]]; then
    echo "Use: delete_model.sh <model_name>"
    exit 1;
fi

MODEL_NAME=$1

# Post the JSON file to the model path.
curl -XGET http://localhost:8909/model/$MODEL_NAME/delete