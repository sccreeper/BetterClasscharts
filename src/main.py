from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from kivymd.app import MDApp

import util


Builder.load_file('views/main.kv')

class MainScreen(Screen):

    def test():
        pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = MainScreen()

    def build(self):

        #Init button callbacks, other shit etc.

        self.screen.ids.homework_scroll.add_widget(MDLabel(text='test', halign='center'))

        return self.screen


    def on_start(self):
        self.fps_monitor_start()

        #Begin initial loading/generation

if __name__ == "__main__":  
    MainApp().run()