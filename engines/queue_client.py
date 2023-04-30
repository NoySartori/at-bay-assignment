from engines.db_client import scan_object_mock

queued_task_mock = {'task_id': scan_object_mock.scan_id}

class QueueClient:
    def enqueue(self, task_id):
        global queued_task_mock
        return queued_task_mock

    def dequeue(self):
        global queued_task_mock
        return queued_task_mock
