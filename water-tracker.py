import json
import os
from datetime import datetime


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