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

#Logic

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

#Change the colour and write it to the config.
def change_theme_colour(hex, name):

    #Change in UI

    globals.app_object.theme_cls.primary_palette = name #Main UI

    #Bodge to get bottom navigation to change

    globals.screen.ids.bottom_navigation.switch_tab(globals.CURRENT_TAB)

    #Change in config

    globals.CURRENT_CONFIG["accent_colour"] = hex
    globals.CURRENT_CONFIG["accent_name"] = name

    util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.CURRENT_CONFIG))

def change_dark_mode(*args):

    #Change config

    globals.CURRENT_CONFIG["dark_mode"] = not globals.CURRENT_CONFIG["dark_mode"]
    util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.CURRENT_CONFIG))

    #Update UI
    
    globals.app_object.theme_cls.theme_style = "Dark" if globals.CURRENT_CONFIG["dark_mode"] else "Light"


#Changing screens

def show_settings_screen(*args):

    #Update information

    globals.screen_manager.get_screen("SettingsScreen").student_code = globals.CURRENT_CONFIG['code']
    globals.screen_manager.get_screen("SettingsScreen").student_name = globals.API_CLIENT.student_info["data"]["name"]

    #Transition
    
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "SettingsScreen"

def show_about_screen(*args):
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "AboutScreen"

def show_appearance_screen(*args):
    #Update data

    globals.appearance_screen.ids.colour_picker.text = globals.CURRENT_CONFIG["accent_name"]

    globals.appearance_screen.ids.dark_check.children[0].bind(active=does_nothing)

    if globals.CURRENT_CONFIG["dark_mode"]: globals.appearance_screen.ids.dark_check.children[0].active = True
    else: globals.appearance_screen.ids.light_check.children[0].active = True

    globals.appearance_screen.ids.dark_check.children[0].bind(active=change_dark_mode)

    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "AppearanceScreen"

def does_nothing(*args):
    pass

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

def show_sync_screen(*args):
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "SyncScreen"