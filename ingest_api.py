from flask import Flask, request, jsonify

from models.scan import Scan, ScanStatus

from engines.db_client import DbQuery
from engines.queue_client import QueueClient

app = Flask(__name__)

@app.route('/api/ingest', methods=['POST'])
def ingest_request():
    request_data = request.get_json()
    url = request_data['url']
    scan = Scan(url=url, status=ScanStatus.ACCEPTED)
    initiated_scan = insert_request_to_db(scan)
    enqueue(initiated_scan.scan_id)
    return jsonify(initiated_scan.scan_id)


def insert_request_to_db(scan: Scan):
    db_query = DbQuery()
    update_scan = db_query.create_scan(scan)
    return update_scan


def enqueue(scan_id):
    queue_client = QueueClient()

    return queue_client.add_scan_task_to_queue(scan_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
