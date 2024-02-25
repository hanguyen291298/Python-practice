import requests
import os
from datetime import datetime
APP_ID = os.environ.get("NT_APP_ID")
API_KEY = os.environ.get("NT_API_KEY")
TOKEN = os.environ.get("NT_TOKEN")
DATE = datetime.now().date().strftime("%y/%m/%d")
TIME = datetime.now().strftime("%X")


exercise_nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
excercise_text = input("Which excerise did you do: ")
excercise_paras = {
    "query": excercise_text,
    "gender": "female",
    "weight_kg": 38,
    "height_cm": 155,
    "age": 25
}
header_1 = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}
response_1 = requests.post(url=exercise_nutrition_endpoint, json=excercise_paras, headers=header_1)
data = response_1.json()
print(data)


sheety_endpoint = "https://api.sheety.co/aba4dd63e99c1583111eaae9b63ffcd5/workoutTracking/workouts"
for excercise in data["exercises"]:
    EXERCISE = excercise["name"]
    DURATION = excercise["duration_min"]
    CALORIES = excercise["nf_calories"]

    sheety_paras = {
    "workout": {
       "date": DATE,
       "time": TIME,
       "exercise": EXERCISE,
       "duration": DURATION,
       "calories": CALORIES
        }
    }
    header_2 = {
        "Authorization": TOKEN
    }
    response_2 = requests.post(url=sheety_endpoint, json=sheety_paras, headers=header_2)
    print(response_2.text)
