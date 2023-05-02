from engines.db_client import DbQuery
from engines.queue_client import QueueClient

from time import sleep

from models.scan import ScanStatus

while True:
    queue_client = QueueClient()
    db_client = DbQuery()

    print("Waiting for scans")
    scan_task = queue_client.get_scan_task()

    scan_id = scan_task['task_id']
    print(f"Got scan with id {scan_id}")

    scan_obj = db_client.get_scan(scan_id)
    print("Got scan object")
    print(scan_obj)

    db_client.update_scan_status(scan_id, ScanStatus.RUNNING)

    sleep(10)

    db_client.set_scan_as_finished(scan_id, ScanStatus.COMPLETE)

    print('Finished')





