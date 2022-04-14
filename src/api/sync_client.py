import requests

class SyncClient:
    _session_id: str
    student_code: str
    student_dob: str

    def __init__(self, code, dob) -> None:
        
        self.student_code = code
        self.dob = dob
