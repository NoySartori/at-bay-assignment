from datetime import datetime

from models.scan import Scan, ScanStatus

import sqlite3


class DbQuery:
    def __init__(self):
        with self.__get_conn__() as con:
            cur = con.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS scans (scan_id INTEGER PRIMARY KEY AUTOINCREMENT, url TEXT NOT NULL, status INTEGER NOT NULL, finish_time INTEGER)")

            con.commit()

    def __get_conn__(self):
        return sqlite3.connect("scans.db")

    def create_scan(self, scan: Scan) -> Scan:
        with self.__get_conn__() as con:
            cur = con.cursor()

            cur.execute(f"INSERT INTO scans (url,status) VALUES ('{scan.url}',{scan.status.value})")

            new_row_id = cur.lastrowid

            con.commit()

            inserted_row, = cur.execute(f"SELECT scan_id FROM scans WHERE rowid = {new_row_id}").fetchone()

            scan.scan_id = inserted_row

        return scan

    def get_scan(self, scan_id: int) -> Scan | None:
        with self.__get_conn__() as con:
            cur = con.cursor()

            res = cur.execute(
                f"SELECT scan_id, url, status, finish_time FROM scans WHERE scan_id = {scan_id}").fetchone()

            if res:
                row_scan_id, url, status, finish_time = res
                return Scan(scan_id=row_scan_id, url=url, status=ScanStatus(status), finish_time=finish_time)

        return None

    def delete_scan(self, scan_id: int):
        with self.__get_conn__() as con:
            cur = con.cursor()
            cur.execute(f"DELETE scans where scan_id={scan_id}")
            con.commit()

    def update_scan_status(self, scan_id: int, status: ScanStatus):
        with self.__get_conn__() as con:
            cur = con.cursor()
            cur.execute(f"UPDATE scans SET status={status.value} WHERE scan_id={scan_id}")
            con.commit()

    def set_scan_as_finished(self, scan_id: int, status: ScanStatus):
        now = datetime.now().timestamp()

        with self.__get_conn__() as con:
            cur = con.cursor()

            cur.execute(f"UPDATE scans SET status={status.value}, finish_time={now} WHERE scan_id={scan_id}")
            con.commit()
