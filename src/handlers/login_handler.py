import json
import requests

from kivy.logger import Logger

import globals
from api.client import StudentClient, check_code

def login():
    SUCCESS = False
    
    Logger.info("Application: Logging in...")
    
    if not check_code(globals.login_screen.ids.code.text):
        pass #TODO Do something here
    else:
        #Init API client with values from UI
        globals.API_CLIENT = StudentClient(
            globals.login_screen.ids.code.text, 
            (
                int(globals.login_screen.ids.day.text),
                int(globals.login_screen.ids.month.text),
                int(globals.login_screen.ids.year.text)
            )
        )

        #Login
        globals.API_CLIENT.login()

        #Successful or not
        if globals.API_CLIENT.logged_in: SUCCESS = True
        else: SUCCESS = False

        #Finish logging in and log result to console
        
        globals.screen_manager.current = "MainScreen"

        Logger.info("Application: Login successful.")

