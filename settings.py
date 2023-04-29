import os

RUNNING_TASKS_FILE_PATH = os.environ.get('AUDIO_DIRECTORY', 'storage/tasks/running_tasks.json')
AUDIO_DIRECTORY = os.environ.get('AUDIO_DIRECTORY', 'storage/audios')
APP_STATE_FILE_PATH = os.environ.get('APP_STATE_FILE_PATH', 'storage/app_state.json')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', "redis://127.0.0.1:6379/0")
