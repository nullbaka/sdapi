import os
import json

from settings import RUNNING_TASKS_FILE_PATH, APP_STATE_FILE_PATH


def write_json(file_path, json_obj):
    with open(file_path, 'w') as file:
        json.dump(json_obj, file)
    return True


def read_json(file_path):

    if not os.path.isfile(file_path):
        return {}

    with open(file_path, 'r') as file:
        try:
            json_obj = json.load(file)
        except json.decoder.JSONDecodeError:
            json_obj = {}

    return json_obj


def add_to_running_tasks(task_name, task_id):
    running_tasks = read_json(RUNNING_TASKS_FILE_PATH)
    running_tasks[task_name] = task_id
    write_json(RUNNING_TASKS_FILE_PATH, running_tasks)


def remove_from_running_tasks(task_name):
    running_tasks = read_json(RUNNING_TASKS_FILE_PATH)
    running_tasks.pop(task_name)
    write_json(RUNNING_TASKS_FILE_PATH, running_tasks)


def update_app_state(key_name, value):
    app_state = read_json(APP_STATE_FILE_PATH)
    app_state[key_name] = value
    write_json(APP_STATE_FILE_PATH, app_state)


def are_models_preloaded():
    app_state = read_json(APP_STATE_FILE_PATH)
    return app_state.get('are_models_loaded', False)
