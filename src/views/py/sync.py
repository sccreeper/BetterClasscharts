from kivy.uix.screenmanager import Screen, SlideTransition

import globals

class SyncScreen(Screen):
    
    def go_back(*args):
        
        #Transition
        
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "SettingsScreen"

    def enable_sync(self, *args):
        pass

    def start_sync(self, *args):
        pass



    