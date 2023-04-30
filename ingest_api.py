from flask import Flask, request
from waitress import serve

from models.scan import Scan, ScanStatus

from engines.db_client import DbQuery
from engines.queue_client import QueueClient

app = Flask(__name__)

db_query = DbQuery()
queue_client = QueueClient()


@app.route('/api/ingest', methods=['POST'])
def ingest_request():
    request_data = request.get_json()
    url = request_data['url']
    scan = Scan(url=url, status=ScanStatus.ACCEPTED.value)
    initiated_scan = insert_request_to_db(scan)
    queued_task = enqueue(initiated_scan.scan_id)
    return initiated_scan.scan_id


def insert_request_to_db(scan: Scan):
    update_scan = db_query.create_scan(scan)
    return update_scan


def enqueue(scan_id):
    return queue_client.enqueue(scan_id)


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=3000, debug=True)
