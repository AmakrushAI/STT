# Overview
This repository is based on https://github.com/AI4Bharat/IndicWav2Vec. \
There are few changes made in code to make the repo run.

# Deployment
Run the shell script 'deploy.sh'. It will install libraries and start the API.

# Testing the API
Below curl is an example where we can send wav url to API
> curl --location 'http://localhost:5000/infer_ulca_or' --header 'Content-Type: application/json' --data '{
    "config": {
        "language":{
          "sourceLanguage": "or"
        },
        "transcriptionFormat": {"value":"transcript"},
        "audioFormat": "wav"
    },
    "audio": [{
        "audioUri": "https://github.com/djgupta/flat_files/raw/main/odiya_test.wav"
    }]
}'

# Benchmarking API
Locust is used for API performance testing
Below command needs to be fired, it would be better to run this command on another system
> locust --headless -H http://127.0.0.1:8000 -u 10 -r 2 --run-time 180 --csv=t5
