from api.client import StudentClient
from kivy.uix.screenmanager import Screen

# Globals

API_CLIENT: StudentClient

HOMEWORK_LENGTH =  -1

screen_manager = None

#UI

screen = None
login_screen = None
homework_details_screen = None
settings_screen = None

about_screen = None
licenses_screen = None
appearance_screen = None

splash_screen = None
loading_circle_screen = None

app_object = None

CURRENT_TAB = "activity"

#Config

CONFIG_PATH = None
DEFAULT_CONFIG = {
    
    "set_up" : False,
    "code" : "",
    "dob" : (0, 0, 0), #D, M, Y
    "dark_mode": False,
    "accent_name": "Blue", #See: https://kivymd.readthedocs.io/en/latest/themes/theming/index.html#kivymd.theming.ThemeManager.primary_palette
    "accent_colour": "2962FF" #Default blue colour, see ACCENT_COLOURS: Dict

}

CURRENT_CONFIG = DEFAULT_CONFIG #So certain UI elements load.

ACCENT_COLOURS = [ #Used for displaying colours in UI

    ["Red", "D50000"],
    ["Pink", "C51162"],
    ["Purple", "AA00FF"],
    ["Blue", "2962FF"],
    ["Teal", "004D40"],
    ["Green", "2E7D32"],
    ["Orange", "E65100"],

]

#TODO: Save this to config and load it in the future
SHOW_HANDED_IN = True
SHOW_DUE = True
HW_CACHE = None #Cache the homework locally to avoid requesting it from the API each time.