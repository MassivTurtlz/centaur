import json


def get_json(SAVE_FILE):
    with open(SAVE_FILE, 'r') as read_file:
        read_data = json.load(read_file)
        return read_data


def update_json(json_data, SAVE_FILE):
        with open(SAVE_FILE) as read_file:
            read_data = json.load(read_file)
        with open(SAVE_FILE, 'w') as f:
            read_data.append(json_data)
            f.write(json.dumps(read_data, indent=2))
