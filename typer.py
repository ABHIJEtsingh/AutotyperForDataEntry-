import json
import pyautogui
import time  # Import the time module

import json
import pyautogui

# Load the data from the JSON file
with open('105th.json') as f:
    data_file = json.load(f)
    

# Define the order in which you want to input the data, excluding "Height" and "Weight"
input_order = [
    "Name",
    "Gender",
    "Age",
    "Marital Status",
    "Education",
    "Detail",
    "Occupation",
    "Religion",
    "Caste",
    "Sub Caste",
    "Gothram",
    "Mother Tongue",
    "Horoscope Match",
    "Star",
    "Rassi/Moon Sign",
    "Dhosham / Magalik",
    "Height",
    "Weight",
    "Height",
    "Weight",
    "Height",
    "Citizen of",
    "Home State",
    "Home State",
    "Country Living",
    "Home State",
    "Name",
    "Name",
    "Body Type",
    "Complexion",
    "Physical Status",
    "Eating Habit",
    "Smoke Habit",
    "Drink Habit",
    "Family Value",
    "Family",
    "Family Status",
    "Annual Income",
    "About Family",
    "More Description",
    "Expectations"
]
additional_text = {
    "password": "1234",
    "How to know about us": "friends",
}

# Find the starting position for typing
x, y = pyautogui.locateCenterOnScreen("field.png", confidence=0.8)
pyautogui.moveTo(x, y, duration=1)
pyautogui.leftClick()

# Loop through the data in the specified order and type it
for field in input_order:
    if field not in [ "Height", "Weight"]:
        value = data_file.get(field, "")  # Get the value from the JSON data, default to an empty string
        if field in additional_text:
            value += additional_text[field]
        pyautogui.typewrite(value)
    pyautogui.press("tab")
