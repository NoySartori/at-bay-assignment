from engines.db_client import DbQuery
from models.scan import Scan, ScanStatus

db_client = DbQuery()

new_scan = db_client.create_scan(Scan(status=ScanStatus.ACCEPTED, url='https://virus.com'))
print(new_scan)