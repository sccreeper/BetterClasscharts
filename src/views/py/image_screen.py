#For viewing images on HW
from kivy.uix.screenmanager import Screen, FallOutTransition
from kivy.properties import ObjectProperty

import globals

class ImageScreen(Screen):
    image_data = ObjectProperty()

    def close_screen(self, *args):

        globals.screen_manager.transition = FallOutTransition(duration=0.25)
        globals.screen_manager.current = "MainScreen"