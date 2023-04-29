import os
import time
from fastapi import FastAPI
from fastapi.responses import FileResponse

from models import Prompt
from tasks import preloader, audio_generator
from json_manager import read_json
from constants import RUNNING_TASKS_FILE_PATH, AUDIO_DIRECTORY


app = FastAPI()


@app.get("/")
def index():
    return {
        "name": "Uttaran Wary",
        "application": True
    }


@app.get("/preload-models")
def preload_models():
    task_name = preloader.name

    running_tasks = read_json(RUNNING_TASKS_FILE_PATH)
    if task_name in running_tasks:
        return {
            "success": False,
            "message": "Preloading is in progress."
        }

    _ = preloader.delay()
    return {
        "success": True,
        "message": "Preloading started."
    }


@app.post("/generate-audio")
def generate_audio(prompt: Prompt):
    task_name = audio_generator.name

    running_tasks = read_json(RUNNING_TASKS_FILE_PATH)
    if task_name in running_tasks:
        return {
            "success": False,
            "message": "Generating an audio. Please try again later."
        }

    prompt_text = prompt.text

    time_now_obj = time.time()
    time_now_str = str(time_now_obj).split('.')[0]

    filename = f"audio_{time_now_str}.wav"

    path = f"{AUDIO_DIRECTORY}/{filename}"
    audio_generator.delay(prompt_text, path)

    return {
        "success": True,
        "filename": filename,
        "message": f"Please visit localhost:8000/{filename} to download your audio."
    }


@app.get("/download-audio/{filename}")
def get_audio(filename):
    file_path = f"{AUDIO_DIRECTORY}/{filename}"

    if not os.path.isfile(file_path):
        return {
            "success": False,
            "message": "File does not exist."
        }

    return FileResponse(file_path)
