#Functions shown in the 3 dots menu

from kivy.app import App
from kivy.uix.screenmanager import SlideTransition

import globals

def show_settings_screen(*args):

    #Update information

    globals.screen_manager.get_screen("SettingsScreen").student_code = globals.CURRENT_CONFIG['code']

    #Transition
    
    globals.screen_manager.transition = SlideTransition(direction="left", duration=0.25)
    globals.screen_manager.current = "SettingsScreen"

def logout(*args):
    pass