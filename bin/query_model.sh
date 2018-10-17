#!/usr/bin/env bash

# This script is used to query an existing model.

echo "Early version of the curl tools for models."

if [[ -z $1 ]] || [[ -z $2 ]]; then
    echo "Use: query_model.sh <text_to_classify> <model_name>"
    exit 1;
fi

JSON={\""Text\"":\""$1\""}
MODEL_NAME=$2


# Post the JSON file to the model path.
curl -XPOST http://localhost:8909/model/$MODEL_NAME/classify -d "$JSON" -H "Content-Type: application/json"