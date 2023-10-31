import requests

parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 19,
}

response_questions = requests.get(url="https://opentdb.com/api.php", params=parameters)
response_questions.raise_for_status()
question_data = response_questions.json()["results"]
