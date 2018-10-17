#!/usr/bin/env bash

# This script is used to create a new model.

echo "Early version of the curl tools for models."

if [[ -z $1 ]] || [[ -z $2 ]]; then
    echo "Use: create_model.sh <json_file> <model_name>"
    exit 1;
fi

JSON_FILE=$(cat $1)
MODEL_NAME=$2

echo $JSON_FILE
echo $MODEL_NAME

# Post the JSON file to the model path.
curl -XPOST http://localhost:8909/model/$MODEL_NAME/create -d "$JSON_FILE" -H "Content-Type: application/json"
