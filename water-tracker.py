import json
import os
from datetime import datetime
import platform

DATA_FILE = "water_data.json"
WATER_GOAL = 6 #cups

def load_data():
    """Load data from JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    """Save data to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def get_today_key():
    """Get the current date as a string key."""
    return datetime.now().strftime("%Y-%m-%d")

def clear_screen():
    """Clear the terminal screen."""
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
    """Set the daily water intake goal based on user input."""
    clear_screen()
    print("How many cups of water would you like to aim for each day?")
    while True:
        # Loop to prompt user for a valid goal value.
        # If a valid goal amount is entered, it is saved to the JSON file.
        goal = input("Enter your daily goal (cups):\n")
        if goal.isdigit() and int(goal) > 0:
            data['goal'] = int(goal)
            save_data(data)
            if int(goal) == 1:
                print(f"\nYour new daily goal is {data['goal']} cup.")
            else:
                print(f"\nYour new daily goal is {data['goal']} cups.")
            break
        else:
            print("\nPlease enter a valid number greater than zero!\n")

while True:
    # Main loop that continuously displays the menu and handles user input
    today = get_today_key()
    if today not in data:
        data[today] = 0
        save_data(data)

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

    # Ensures valid main menu option is entered (1-5)
    while True:
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 0 < int(choice) < 6:
            break
        else:
            print("\nPlease enter a valid number between 1-5!\n")

    if choice == "1":
        clear_screen()
        # Loop to validate water amount input (must be a positive number)
        while True:
            amount = input("How much water (cups) did you drink?\n")
            if amount.isdigit() and int(amount) > 0:
                amount = int(amount)
                data[today] += amount
                save_data(data)
                if amount == 1:
                    print(f"\nAdded {amount} cup.")
                else:
                    print(f"\nAdded {amount} cups.")
                break
            else:
                print("\nPlease enter a valid number greater than zero!\n")

    elif choice == "2":
        clear_screen()
        # Loop to confirm whether user really wants to reset 'today's total' and ensure valid user input 
        while True:
            confirm = input("Are you sure you want to reset today's total? (y/n): ").lower()
            if confirm == 'y':
                data[today] = 0
                save_data(data)
                print("\nToday's total has been reset.")
                break
            elif confirm == 'n':
                print("\nReset cancelled.")
                break
            else:
                print("\nPlease enter 'y' for yes or 'n' for no.\n")

    elif choice == "3":
        clear_screen()
        if data['goal'] == 0:
            print("Goal is set to 0, cannot calculate progress.")
        else:
            percent = (data[today] / data['goal']) * 100
            print(f"Progress: {percent:.1f}% of {data['goal']} cup goal.")

    elif choice == "4":
        set_goal()

    elif choice == "5":
        clear_screen()
        print("Stay hydrated, goodbye!\n")
        break