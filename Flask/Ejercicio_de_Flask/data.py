import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FINAL_JSON_FILE = os.path.join(BASE_DIR, "task.json")

def read_json():
    data_empty = []

    if not os.path.exists(FINAL_JSON_FILE):
        return data_empty

    with open(FINAL_JSON_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            return data_empty

def save_json(data):
    with open(FINAL_JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
