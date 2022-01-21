#Logic for settings

#Kivy libaries

from kivy.app import App
from kivy.logger import Logger

from kivy.uix.screenmanager import SlideTransition, NoTransition
from kivymd.uix.dialog import MDDialog

#System libs

import os, json

#Project libs

import util
import globals

def show_settings_screen(*args):

    #Update information

    globals.screen_manager.get_screen("SettingsScreen").student_code = globals.CURRENT_CONFIG['code']

    #Transition
    
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "SettingsScreen"

def logout(*args):

    Logger.info("Application: Logging out...")

    #Set clear current and saved config.

    globals.CURRENT_CONFIG["set_up"] = False
    globals.CURRENT_CONFIG["code"] = ""
    globals.CURRENT_CONFIG["dob"] = (0,0,0)

    util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.CURRENT_CONFIG))

    # "Delete" API client

    globals.API_CLIENT = None

    #Switch to login screen

    globals.screen_manager.transition = NoTransition()
    globals.screen_manager.current = "LoginScreen"

    Logger.info("Application: Logged out!")

def show_about_screen(*args):
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "AboutScreen"

def show_licenses_screen(*args):
    
    #Update text
    try:
        globals.screen_manager.get_screen("LicensesScreen").license_text = util.read_file("res/licenses.txt")
    except FileNotFoundError:
        globals.screen_manager.get_screen("LicensesScreen").license_text = util.read_file("src/res/licenses.txt")
    except:
        globals.screen_manager.get_screen("LicensesScreen").license_text = "No licenses were included!"
    
    #Transition
    
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "LicensesScreen"
