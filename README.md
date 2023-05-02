# at-bay-assignment

## Setup
It is recommended to have a venv. Example -
`python3.11 -m venv venv`

Then, install requirements -
`python -m pip install -r requirements.txt`

## Run
- ingest_api.py run on port 3000 
- status_api.py run on port 3001
- processor.py doesn't have a server, it listens to the queue

## Usage
To start a scan request, send an HTTP POST JSON request as such -
`{"url":"https://virus2000.com"}`
to http://localhost:3000/api/ingest.

The response will give you the task id.

You can use `http://localhost:3001/api/status/<scan_id>` with the returned task_id to check status.

## Architecture
![diagram](https://raw.githubusercontent.com/NoySartori/at-bay-assignment/main/architecture.drawio.png)
