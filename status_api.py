from flask import Flask, jsonify

from engines.db_client import DbQuery
from models.scan import ScanStatus

app = Flask(__name__)

@app.route('/api/status/<scan_id>', methods=['GET'])
def get_scan_status(scan_id):
    db_query = DbQuery()
    db_res = db_query.get_scan(scan_id)

    scan_status = db_res.status if db_res is not None else ScanStatus.NOT_FOUND.value

    return jsonify(scan_status.value)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
