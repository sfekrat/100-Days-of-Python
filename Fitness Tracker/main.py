import requests as re
from datetime import datetime
import os

APP_ID = os.environ.get("FT_APP_ID")
API_KEY = os.environ.get("FT_API_KEY")
API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
SHEETY_URL = os.environ.get("SHEETY_ENDPOINT")
# Optional Parameters
WEIGHT_KG = 80
HEIGHT_CM = 190
AGE = 35

header = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = re.post(url=API_ENDPOINT, json=params, headers=header)
response.raise_for_status()

result = response.json()
cur_date = datetime.now().strftime("%d/%m/%Y")
cur_time = datetime.now().strftime("%X")

sheety_header = {
    "Content-Type": "application/json",
    "Authorization": AUTH_TOKEN
}

for exercise in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": cur_date,
            "time": cur_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = re.post(url=SHEETY_URL, json=sheet_inputs, headers=sheety_header)
    sheety_response.raise_for_status()
    print(sheety_response.text)
