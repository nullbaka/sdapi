# sdapi

### Introduction
- Due to limited memory, I decided to implemented this project with asynchronous tasks
- Audios are generated in background and can be retrieved later

### Dev environment:
- Mac M1
- Python 3.9
- Docker Desktop 4.16.2 (95914)


### Instructions to run
- `docker compose build`
- `docker compose up`


### Endpoints
- **GET** [localhost:8000/](localhost:8000/)
- **POST** [localhost:8000/preload-models](localhost:8000/preload-models)
- **POST** [localhost:8000/generate-audio](localhost:8000/generate-audio)
- **GET** [localhost:8000/download-audio](localhost:8000/download-audio)


### Screen Recordings
#### Models aren't preloaded
https://user-images.githubusercontent.com/18743192/235309733-2d840d89-bd86-4b0a-8ae2-68e705ec8f1f.mov

#### Preloading models
https://user-images.githubusercontent.com/18743192/235309747-cf585039-ccf4-4fa9-bb99-a2ade5be7c1f.mov

#### Generating audio
https://user-images.githubusercontent.com/18743192/235309771-ec4bd9e2-89c7-4cb0-91bb-8381bd35b025.mov

#### Retrieving audio
https://user-images.githubusercontent.com/18743192/235309783-8f7811aa-487f-47c4-bc86-32e84ec36ebf.mov

