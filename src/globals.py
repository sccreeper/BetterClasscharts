from api.client import StudentClient
from kivy.uix.screenmanager import Screen

# Globals

API_CLIENT: StudentClient

HOMEWORK_LENGTH =  -1

screen_manager = None

screen = None
login_screen = None
homework_details_screen = None

CONFIG_PATH = None
DEFAULT_CONFIG = {
    
    "set_up" : False,
    "code" : "",
    "dob" : (0, 0, 0), #D, M, Y
    "dark_mode": False

}

CURRENT_CONFIG = None

#TODO: Save this to config and load it in the future
SHOW_HANDED_IN = True
SHOW_DUE = True