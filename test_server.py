from requests import post
from json import loads
model_parameters = None

endpoint = "https://immense-dusk-95991.herokuapp.com"
with open('training_examples.json') as train_file:
    train_data = loads(train_file.read())

response = post(f"{endpoint}/train", json=train_data)
print(response)
if response.ok:
    model_parameters = response.json()
    print(model_parameters)

if model_parameters is not None:
    example_query = {
        "text":"this is a test",
        "weights":model_parameters.get("weights"),
        "labels":model_parameters.get("labels"),
    }

    response = post(f"{endpoint}/label", json=example_query)
    print(response)
    if response.ok:
        print(response.json())