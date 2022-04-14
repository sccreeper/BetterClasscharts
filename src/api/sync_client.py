import json
import requests

import globals
from . import SYNC_ENDPOINT
class SyncClient:
    session_id: str
    student_code: str
    student_dob: str

    def __init__(self, code, dob) -> None:
        
        self.student_code = code
        self.student_dob = dob

    def login(self):

        payload = {
            "code" : self.student_code,
            "dob" : self.student_dob
        }

        r = requests.post(f"{globals.SYNC_PROTOCOL}://{globals.CURRENT_CONFIG['sync_url']}{SYNC_ENDPOINT.LOGIN}", data=payload)

        jsonResp = json.loads(r.text)

        self.session_id = jsonResp["data"]["session_id"]

