import os
import json

from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.properties import StringProperty, BooleanProperty

from handlers import open_url

import globals
import util

class DevScreen(Screen):
    build_id = util.read_file("src/res/build_id.txt")
    fps_enabled = BooleanProperty()

    def open_commit(self,*args):
        open_url.launch_webbrowser(f"https://github.com/sccreeper/BetterClasscharts/commit/{self.build_id}")

    def enable_fps(self, *args):

        print("Hello World")
        
        globals.CURRENT_CONFIG["dev"]["fps_enabled"] = self.ids.fps_switch.active

        if globals.CURRENT_CONFIG["dev"]["fps_enabled"]:
            globals.app_object.start_fps()
        else:
            globals.app_object.stop_fps()

        #Save config

        util.write_file(os.path.join(globals.CONFIG_PATH, "config.json"), json.dumps(globals.CURRENT_CONFIG))

    def go_back(*args):
        
        #Transition
        
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "SettingsScreen"