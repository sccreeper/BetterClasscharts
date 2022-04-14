from kivy.uix.screenmanager import Screen, SlideTransition

from handlers.sync import start_sync, enable_sync

import globals

class SyncScreen(Screen):
    
    def go_back(*args):
        
        #Transition
        
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "SettingsScreen"

    def enable_sync(self, *args):
        enable_sync(not self.ids.sync_switch.active)

    def start_sync(self, *args):
        start_sync()



    