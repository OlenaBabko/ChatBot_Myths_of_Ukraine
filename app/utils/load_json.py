import json
import random
import datetime

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def choose_random_element_by_date(json_array):
    if not json_array:
        return None

    current_day = datetime.datetime.now().timetuple().tm_yday
    random.seed(current_day)

    return random.choice(json_array)