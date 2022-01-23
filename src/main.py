from sys import path
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition, Screen, ScreenManager, SlideTransition
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp

from kivy.core.window import Window
from kivy.utils import platform
from kivy.logger import Logger

from api.client import StudentClient

from views.py import homework_view
from views.py.login import LoginScreen
from views.py.settings import SettingsScreen
from views.py.about import AboutScreen, AboutItem, LicensesScreen
from views.py.appearance import AppearanceScreen

import globals
from handlers import display_homework_tiles, display_activity, display_timetable, display_homework_details, settings

import util
import os, pathlib, json

#Subscreens

#Homework
#TODO automate this
Builder.load_file('views/kv/homework.kv')
Builder.load_file('views/kv/homework_details.kv')
Builder.load_file('views/kv/attachment_tile.kv')
Builder.load_file('views/kv/homework_sorter.kv')

#Main screens

Builder.load_file('views/kv/login.kv')
Builder.load_file('views/kv/main.kv')
Builder.load_file('views/kv/settings.kv')
Builder.load_file('views/kv/about.kv')
Builder.load_file('views/kv/appearance.kv')

class MainScreen(Screen):

    def test():
        pass

#Homework screens
class HomeworkScreen(Screen):
    pass

class HomeworkDetailsScreen(Screen):
    pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.bind(on_key_up=self.handle_keyup)

        #Init screens
        
        globals.screen_manager = ScreenManager(transition=NoTransition())

        globals.screen = MainScreen(name="MainScreen")
        globals.login_screen = LoginScreen(name="LoginScreen")
        globals.settings_screen = SettingsScreen(name="SettingsScreen")
        globals.about_screen = AboutScreen(name="AboutScreen")
        globals.licenses_screen = LicensesScreen(name="LicensesScreen")
        globals.appearance_screen = AppearanceScreen(name="AppearanceScreen")

        globals.homework_details_screen = HomeworkDetailsScreen(name="HomeworkDetailsScreen")

        globals.screen.ids.homework_screen_manager.add_widget(HomeworkScreen(name='HomeworkScreen'))

        globals.screen_manager.add_widget(globals.screen)
        globals.screen_manager.add_widget(globals.login_screen)
        globals.screen_manager.add_widget(globals.settings_screen)
        globals.screen_manager.add_widget(globals.about_screen)
        globals.screen_manager.add_widget(globals.licenses_screen)
        globals.screen_manager.add_widget(globals.appearance_screen)
        globals.screen.ids.homework_screen_manager.add_widget(globals.homework_details_screen)

        #Bind buttons to update screen
        globals.screen.ids.homework_button.bind(on_tab_press=display_homework_tiles.display_hw)
        globals.screen.ids.activity_button.bind(on_tab_press=display_activity.display_activity)
        globals.screen.ids.timetable_button.bind(on_tab_press=display_timetable.display_timetable)

    def build(self):

        #Config
        globals.CONFIG_PATH = self.user_data_dir

        #Logging in + config
        
        Logger.info("Application: Logging in...")

        #Check to see if config exists, if not, create new.
        if not os.path.exists(os.path.join(globals.CONFIG_PATH, "config.json")):
            
            if not os.path.exists(globals.CONFIG_PATH): os.mkdir(globals.CONFIG_PATH)
            pathlib.Path(os.path.join(globals.CONFIG_PATH, "config.json"))

            util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.DEFAULT_CONFIG))
        
        #
        if (
            os.path.exists(os.path.join(globals.CONFIG_PATH, "config.json")) 
            and                                                                                              #config exists but not set up
            json.loads(util.read_file(os.path.join(globals.CONFIG_PATH, "config.json")))["set_up"] == False
        ):
            globals.screen_manager.current = "LoginScreen"
        
        elif (
            os.path.exists(os.path.join(globals.CONFIG_PATH, "config.json")) 
            and                                                                                            #config exists + set up
            json.loads(util.read_file(os.path.join(globals.CONFIG_PATH, "config.json")))["set_up"] == True
        ):
            
            globals.CURRENT_CONFIG = json.loads(util.read_file(os.path.join(globals.CONFIG_PATH, "config.json")))

            globals.API_CLIENT = StudentClient(globals.CURRENT_CONFIG["code"], globals.CURRENT_CONFIG["dob"])
            globals.API_CLIENT.login()

            #Backwards compatibility

            if not os.path.exists(os.path.join(globals.CONFIG_PATH, "homework_downloads")):
                os.mkdir(os.path.join(globals.CONFIG_PATH, "homework_downloads"))

            #Update config if certain keys aren't present

            if not "accent_name" in globals.CURRENT_CONFIG and not "accent_colour" in globals.CURRENT_CONFIG:
                globals.CURRENT_CONFIG["accent_name"] = "Blue"
                globals.CURRENT_CONFIG["accent_colour"] = "2962FF"

                util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.CURRENT_CONFIG))
        
        #Theming
        
        self.theme_cls.primary_palette = globals.CURRENT_CONFIG["accent_name"]
        self.theme_cls.theme_style = "Dark" if globals.CURRENT_CONFIG["dark_mode"] else "Light"

        return globals.screen_manager


    def on_start(self):
        self.fps_monitor_start()

        globals.screen.ids.bottom_navigation.switch_tab(globals.CURRENT_TAB) #Get wodget to be orange on start
        
    def post_build_init(self,ev):
        if platform == 'android':
            import android # type: ignore
            android.map_key(android.KEYCODE_BACK, 1001)
    
    #Settings transitions
    def show_settings(self, *args):
        settings.show_settings_screen()

    #General purpose show main screen
    def show_main_screen(self, *args):
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "MainScreen"


    
    #Hook onto Android back button event
    #See: https://stackoverflow.com/a/20094268
    
    def handle_keyup(self, *args):

        if args[1] == 1001: #Back on android

            if globals.screen.ids.homework_screen_manager.current == "HomeworkDetailsScreen": #Are we on a homework screen?
                display_homework_details.go_back()
        
                return True
        
        return False


    #self.screen.ids.homework_scroll.rows += 1


if __name__ == "__main__":
    
    globals.app_object = MainApp()
    globals.app_object.run()