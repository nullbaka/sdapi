import os
from celery import Celery
from scipy.io.wavfile import write as write_wav

from bark.bark import preload_models, generate_audio, SAMPLE_RATE

from settings import CELERY_BROKER_URL, CELERY_RESULT_BACKEND
from json_manager import (
    add_to_running_tasks,
    remove_from_running_tasks,
    update_app_state
)


celery = Celery(
    __name__,
    broker=CELERY_BROKER_URL,
    backend=CELERY_RESULT_BACKEND,
)


@celery.task(bind=True, name="preloader")
def preloader(self):
    task_id = self.request.id

    add_to_running_tasks(self.name, task_id)
    preload_models()
    remove_from_running_tasks(self.name)

    update_app_state("are_models_loaded", True)


@celery.task(bind=True, name="audio_generator")
def audio_generator(self, prompt, path):
    task_id = self.request.id

    add_to_running_tasks(self.name, task_id)

    audio_array = generate_audio(prompt)
    write_wav(path, SAMPLE_RATE, audio_array)

    remove_from_running_tasks(self.name)
