from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.behaviors import TouchRippleButtonBehavior
from kivymd.uix.gridlayout import MDGridLayout

from kivy.properties import StringProperty

import globals
from handlers.open_url import launch_webbrowser
from handlers.settings import show_licenses_screen

class AboutItem(TouchRippleButtonBehavior, MDGridLayout):
    text = StringProperty()
    icon = StringProperty()

    def on_press(self):
        if self.icon == "github":
            launch_webbrowser(None, "https://github.com/sccreeper/BetterClasscharts")
        else:
            show_licenses_screen()

class AboutScreen(Screen):
    
    def go_back(*args):

        #Transition
        
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "SettingsScreen"

class LicensesScreen(Screen):

    license_text = StringProperty()
    
    def go_back(*args):

        #Transition
        
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "AboutScreen"
