from argparse import ArgumentError
from datetime import date, datetime, timedelta
from sys import path
from typing import List, NamedTuple, Tuple
import requests
import json
from collections import namedtuple
import time

from api import CLASSCHARTS_URL, ENDPOINT

from kivy.logger import Logger

from api import http_methods
from api.http_methods import GET, POST

class StudentClient:

    _cookies: dict

    code: str
    student_dob: str

    session_id: str #The session, used for authorization
    student_id: int
    student_info: dict

    http_client: requests.Session #Cookies are saved for each request

    logged_in = False

    dummy_client: bool

    def __init__(self, student_code: str, student_dob: tuple):

        self.code = student_code
        self.student_dob = f"{student_dob[0]}/{student_dob[1]}/{student_dob[2]}"
        
        #Other class variables which need to be initialized

        self.session_id = "" 
        self.student_id = 0

        self.http_client = requests.Session()

        if self.code == "dummy" and student_dob == "dummy":
            self.dummy_client = True
        else: 
            self.dummy_client = False 

    def http_request(self, url: str, http_method: int, auth_needed: bool = True, payload=None) -> requests.Response:
        match http_method:
            case http_methods.GET:
                return self.http_client.get(
                    url, 
                    headers={
                        "Authorization" : "Basic " + self.session_id
                    } if auth_needed else {}
                )
            case http_methods.POST:
                return self.http_client.post(
                    url, 
                    headers={
                        "Authorization" : "Basic " + self.session_id
                    } if auth_needed else {},
                    data=payload
                )

    #Endpoints
    
    #Initiates the client and logs it in to ClassCharts
    def login(self):

        start_time = time.time()

        #Check the code to see if it is valid
        if not check_code(self.code):
            #TODO: Handle this properly
            Logger.warning("API: Pupil code not valid!")
            return
        
        payload = {
            "_method" : "POST",
            "code" : self.code,
            "dob": self.student_dob,
            "remember_me" : "1",
            "recaptcha-token": "no-token-available"
        }

        #self.http_client.post(CLASSCHARTS_URL + ENDPOINT.LOGIN, data=payload)

        r = self.http_request(CLASSCHARTS_URL + ENDPOINT.LOGIN, POST, payload=payload, auth_needed=False)

        self.student_info = json.loads(r.text)
        
        #Check wether login was successful or not.
        if not self.student_info["success"] == 1:
            Logger.warning("API: Login failed!")
            self.logged_in = False

            return #TODO Handle properly
        else:
            Logger.info("API: Login successful")
            self.logged_in = True

        #Set variables for login data (session id etc)
        self.student_id = int(self.student_info["data"]["id"])
        self.session_id = self.student_info["meta"]["session_id"]

        self._cookies = r.cookies

        Logger.info(f"API: Logged in {time.time() - start_time} second(s)")

    def get_homework(self) -> List[dict]:

        if self.dummy_client: return []

        data = self.http_request(f"{CLASSCHARTS_URL}/apiv2student/homeworks/{self.student_id}", GET).text

        data = json.loads(data)

        hw_array = []

        for hw in data["data"]:
            hw_array.append(hw)

        return hw_array
    
    def hand_in_homework(self, status_id: int) -> bool:
        """
        Hands in hw according to id.
        Returns: Boolean depending wether request was successful or not.
        """

        if self.dummy_client: return False

        #Logger.info(f"API: Handing in homework {status_id}...")
        
        data = self.http_request(f"{CLASSCHARTS_URL}{ENDPOINT.HW_HAND_IN}{status_id}?pupil_id={self.student_id}", GET).text

        data = json.loads(data)

        if data["success"] == 1:
            Logger.info(f"API: Handing in homework {status_id} SUCCESS")
            return True
        else:
            Logger.warning(f"API: Handing in homework {status_id} FAILURE")
            return False

    
    def get_timetable(self, date: date = None, date_range: Tuple[date] = None) -> List[dict]:
        if self.dummy_client: return False

        if date_range == None: #Only get one date.

            #Get data from endpoint

            data = self.http_request(f"{CLASSCHARTS_URL}{ENDPOINT.TIMETABLE}{self.student_id}?date={date.year}-{date.month:02}-{date.day:02}", GET).text
            data = json.loads(data)

            return data["data"]

        else: #Request multiple dates.
            
            if len(date_range) != 2:
                raise ArgumentError("date_range must be length of 2!")
            else:
                days = []

                for date in range((date_range[1]-date_range[0]).days):

                    d = date_range[0] + timedelta(days=date)
                    
                    data = self.http_request(f"{CLASSCHARTS_URL}{ENDPOINT.TIMETABLE}{self.student_id}?date={d.year}-{d.month:02}-{d.day:02}", GET).text
                    days.append(list(json.loads(data)["data"])) # list() - Make the array 2D. Not required but there for readability.
                
                return days

        raise AttributeError("date and date_range are equal to None!")
    
    def get_activity(self) -> bool:

        """Gets the activity, returns a List[dict]

        Returns:
            List[Dict]: List of all the activity items.
        """

        if self.dummy_client: return []

        data = self.http_request(f"{CLASSCHARTS_URL}{ENDPOINT.ACTIVITY}{self.student_id}", GET).text

        data = json.loads(data)

        data_list = []
        
        #Filter out behaivour only because that's what we support

        for d in data["data"]:
            if d["type"] == "behaviour":
                data_list.append(d)
            else:
                continue

        return data_list

#Func for validating pupil code
def check_code(code: str) -> bool: 
    return json.loads(requests.get(CLASSCHARTS_URL + ENDPOINT.CHECKCODE + code).text)["data"]["has_dob"]