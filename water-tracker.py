import json
import os
from datetime import datetime
import platform


DATA_FILE = "water_data.json"
WATER_GOAL = 6 #cups


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_today_key():
    return datetime.now().strftime("%Y-%m-%d")

def clear_screen():
    os_type = platform.system().lower()
    if os_type == "windows":
        os.system("cls")
    else:
        os.system("clear")

data = load_data()
today = get_today_key()


if 'goal' not in data:
    data['goal'] = WATER_GOAL

if today not in data:
    data[today] = 0


def set_goal():
    clear_screen()
    print("\nHow many cups of water would you like to aim for each day?")
    while True:
        goal = input("Enter your daily goal (cups):\n")
        if goal.isdigit() and int(goal) > 0:
            data['goal'] = int(goal)
            save_data(data)
            print(f"\nYour new daily goal is {data['goal']} cup(s).")
            break
        else:
            print("Please enter a valid number greater than zero!")

