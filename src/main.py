from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from kivymd.app import MDApp
from api.client import StudentClient

from views.py import homework_view

import globals

import util

Builder.load_file('views/kv/homework.kv')
Builder.load_file('views/kv/main.kv')

class MainScreen(Screen):

    def test():
        pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        globals.screen = MainScreen()

    def build(self):

        #Init button callbacks, other shit etc.

        self.theme_cls.material_style = "Dark"

        globals.screen.ids.homework_button.bind(on_tab_press=display_hw)

        return globals.screen


    def on_start(self):
        self.fps_monitor_start()

        #Begin initial loading/generation

        globals.API_CLIENT = StudentClient("********", (0,0,0))

        globals.API_CLIENT.login()

def display_hw(*args):
    data = globals.API_CLIENT.get_homework()

    for hw in data:
    
        globals.screen.ids.homework_scroll.data.append(
            {
                "viewclass" : "HomeworkView",
                "hw_title" : hw["title"],
                "hw_subtitle" : hw["subject"] + " - " + hw["due_date"],
            }
        )


    #self.screen.ids.homework_scroll.rows += 1


if __name__ == "__main__":  
    MainApp().run()