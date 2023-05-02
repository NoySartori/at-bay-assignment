import persistqueue

class QueueClient:
    def __init__(self):
        self.q = persistqueue.SQLiteQueue('scans_queue', auto_commit=True)

    def add_scan_task_to_queue(self, task_id):
        self.q.put({'task_id': task_id})

    def get_scan_task(self):
        self.q.get(block=True)
