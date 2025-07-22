import requests, os
import datetime
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

# Nutritionix
NUTRITIONIX_NLP_NUTRIENTS_URL_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/nutrients"
headers = {
    "Content-Type": 'application/json',
    "x-app-id": os.environ.get("NUTRITIONIX_ID"),
    "x-app-key": os.environ.get("NUTRITIONIX_KEY"),
}
print(headers)
query = input("What did you eat? ")
data = {"query": query}
nutrition_response = requests.post(NUTRITIONIX_NLP_NUTRIENTS_URL_ENDPOINT, headers=headers,json=data )
calories = nutrition_response.json()["foods"][0]["nf_calories"]
print(f"Calories consumed in {query}: {calories}")


NUTRITIONIX_NLP_EXERCISE_URL_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_config = {"query": input("What exercises did you do (you can include duration and/or distance)?: "),}

exercise_response = requests.post(NUTRITIONIX_NLP_EXERCISE_URL_ENDPOINT, headers=headers, json=exercise_config)

 
user_input = exercise_response.json()["exercises"][0]["user_input"]
duration = exercise_response.json()["exercises"][0]["duration_min"]
calories = exercise_response.json()["exercises"][0]["nf_calories"]
print(f"Exercise: {user_input}, Duration: {duration}, Calories: {calories}")

# Save response to a JSON file
with open('nlp_food.json', 'w') as f:
    json.dump(nutrition_response.json(), f, indent=4)
with open('nlp_exercise.json', 'w') as f:
    json.dump(exercise_response.json(), f, indent=4)

# Google Sheets
SHEETY_AUTH_TOKEN = os.environ.get("SHEETY_AUTH_TOKEN")
SHEETY_NUTRITION_ENDPOINT_API = os.environ.get("SHEETY_NUTRITION_URL")
SHEETY_EXERCISE_ENDPOINT_API = os.environ.get("SHEETY_EXERCISE_URL")


headers = {
    "Authorization": SHEETY_AUTH_TOKEN,
}


#Record current date and time
date = datetime.datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")

nutrition_data = {
    "nutrition": {
      "date": formatted_date,
      "time": time,
      "food": query,
      "calories": calories,
    }
  }

workout_data = {
    "exercise": {
      "date": formatted_date,
      "time": time,
      "exercise": user_input,
      "duration": duration,
      "calories": calories,
    }
  }

# Add new row to the spreadsheet with inputted data
#print(headers)
new_response = requests.post(url=SHEETY_NUTRITION_ENDPOINT_API, json=nutrition_data, headers=headers)
new_response = requests.post(url=SHEETY_EXERCISE_ENDPOINT_API, json=workout_data, headers=headers)
#print(new_response.text)



