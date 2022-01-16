import json
import os

from kivy.logger import Logger

import globals
from api.client import StudentClient, check_code
import util

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

        if globals.CURRENT_CONFIG == None:
            globals.CURRENT_CONFIG = json.loads(util.read_file(os.path.join(globals.CONFIG_PATH, "config.json"))) #Assuming that config.json will always exist, probably bad idea.

        #Change config and then write to disk
        globals.CURRENT_CONFIG["code"] = globals.login_screen.ids.code.text

        globals.CURRENT_CONFIG["dob"] = (
            int(globals.login_screen.ids.day.text),
            int(globals.login_screen.ids.month.text),
            int(globals.login_screen.ids.year.text)
        )

        globals.CURRENT_CONFIG["set_up"] = True

        util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.CURRENT_CONFIG))

        #Make homework downloads directory
        if not os.path.exists(os.path.join(globals.CONFIG_PATH, "homework_downloads")):
            os.mkdir(os.path.join(globals.CONFIG_PATH, "homework_downloads"))

        globals.screen_manager.current = "MainScreen"

        Logger.info("Application: Login successful.")

