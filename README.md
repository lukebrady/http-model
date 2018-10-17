![HTTP-MODEL](https://github.com/lukebrains/http-model/blob/master/logo/model_logo.png "HTTP-Model")
# HTTP-Model
An HTTP server for deep learning models and natural language processing.

HTTP-Model is a microservice for your natural language processing models 
that can be updated dynamically via REST and JSON.

This is currently a work in progress. Below are the list of supported algorithms.

#### Supported Algorithms:
+ Naive Bayes

## Usage

Data sets are represented by JSON objects. Below is an example of JSON that would be accepted by the system.
```json
{
  "Data" : 
  [
    [
      "Hello how are you doing today?",
      "salutation"
    ],
    [
      "See you later and have a great day.",
      "valediction"
    ]
  ]
}
```

To create a model run the bin/create_model.sh script.
```bash
$ bin/create_model.sh <json_file> <model_name>
```

To update a model run the bin/update_model.sh script.
```bash
$ bin/update_model.sh <json_file> <model_name>
```

To delete a model run the bin/delete_model.sh script.
```bash
$ bin/delete_model.sh <model_name>
```

## Disclaimer
HTTP-Model is still a work in progress with limited functionality. It is not ready to run in production.

## Contributing
If you would like to contribute to this project send a pull request.

## License

The MIT License (MIT). Please see License File for more information.

