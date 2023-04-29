import os
from celery import Celery
from scipy.io.wavfile import write as write_wav

from bark.bark import preload_models, generate_audio, SAMPLE_RATE

from json_manager import add_to_running_tasks, remove_from_running_tasks


CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', "redis://127.0.0.1:6379/0")
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', "redis://127.0.0.1:6379/0")

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

@celery.task(bind=True, name="audio_generator")
def audio_generator(self, prompt, path):
    task_id = self.request.id

    add_to_running_tasks(self.name, task_id)

    audio_array = generate_audio(prompt)
    write_wav(path, SAMPLE_RATE, audio_array)

    remove_from_running_tasks(self.name)
