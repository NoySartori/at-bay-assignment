from datetime import datetime

from models.scan import Scan, ScanStatus

from uuid import uuid4

scan_object_mock = Scan(status=ScanStatus.ACCEPTED.value, url='https://virus.com')


class DbQuery:
    def create_scan(self, scan: Scan) -> Scan:
        next_id = str(uuid4())

        global scan_object_mock
        scan_object_mock.scan_id = next_id

        scan_object_mock = scan

        return scan_object_mock

    def get_scan(self, scan_id: str) -> Scan:
        global scan_object_mock

        return scan_object_mock

    def delete_scan(self, scan_id: str) -> Scan:
        global scan_object_mock

        return scan_object_mock

    def update_scan_status(self, scan_id: str, status: ScanStatus) -> Scan:
        global scan_object_mock
        scan_object_mock.status = status

        return scan_object_mock

    def set_scan_as_finished(self, scan_id: str, status: ScanStatus) -> Scan:
        global scan_object_mock
        scan_object_mock.status = status
        scan_object_mock.finish_time = datetime.now()

        return scan_object_mock
