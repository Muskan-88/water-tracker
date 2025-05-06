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

while True:
    print("\n~~~~~~~~~~Water Tracker~~~~~~~~~~\n")
    print(f"Today's total: {data[today]} cup(s)")
    print(f"Daily goal: {data['goal']} cup(s)")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("Options:")
    print("1. Add water")
    print("2. Reset total")
    print("3. View progress")
    print("4. Set daily goal")
    print("5. Quit\n")

    while True:
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 0 < int(choice) < 6:
            break
        else:
            print("Please enter a valid number between 1-5!")