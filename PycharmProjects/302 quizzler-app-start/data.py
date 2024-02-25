import requests

paramater = {
    "amount": 10,
    "type": "boolean"
}
response = requests.get(url="https://opentdb.com/api.php?", params=paramater)


data_dict = response.json()

question_data = data_dict["results"]

