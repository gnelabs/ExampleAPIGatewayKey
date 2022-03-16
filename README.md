# ExampleAPIGatewayKey
Example package of an API gateway rest API using key auth.

This cloudformation template will create:
* An API gateway regional endpoint, protected with a key.
* A lambda funciton that returns Hello World!

## Prerequisites

### SAM CLI

This package assumes you have the SAM CLI installed on your developer instance. See: https://github.com/awsdocs/aws-sam-developer-guide/blob/master/doc_source/serverless-sam-cli-install-linux.md

## Usage

Build.

``` bash
# Resolve dependencies and create a .aws-sam/build/ directory.
$ sam build
```

Deploy to cloudformation. Use --guided for the initial install to setup your S3 bucket and what not.

``` bash
# Deploy the application. Use the guided method so you can fill in information about your S3 bucket and region.
$ sam deploy --guided
```

To test the API, grab the API endpoint from the CloudFormation stack output, and the key from API gateway console.

``` python
import requests

# Fill out your API key and endpoint here.
headers = {'x-api-key': '57PykQli0l2WcEtyDiV8i9ihDQPsh9kS9TwGW38Y'}
url = 'https://petwnf7iel.execute-api.us-east-1.amazonaws.com/prod'
r = requests.get(url, headers=headers)
r.status_code
r.json()
```