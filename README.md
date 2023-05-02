# at-bay-assignment

## Setup
It is recommended to have a venv. Example -
`python3.11 -m venv venv`

Then, install requirements -
`python -m pip install -r requirements.txt`

## Run
ingest_api.py run on port 3000 
status_api.py run on port 3001
processor.py doesn't have a server, it listens to the queue

## Architecture
![diagram](https://raw.githubusercontent.com/NoySartori/at-bay-assignment/main/architecture.drawio.png)
