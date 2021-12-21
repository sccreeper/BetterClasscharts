from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel

from kivymd.app import MDApp
from api.client import StudentClient

from views.py import homework_view

import globals
from handlers import display_homework_tiles

import util

Builder.load_file('views/kv/homework.kv')
Builder.load_file('views/kv/homework_details.kv')

Builder.load_file('views/kv/main.kv')

class MainScreen(Screen):

    def test():
        pass

class HomeworkScreen(Screen):
    pass

class HomeworkDetailsScreen(Screen):
    pass

class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        globals.screen = MainScreen()

    def build(self):

        #Init button callbacks, other shit etc.

        #self.theme_cls.theme_style = "Dark"

        globals.screen.ids.homework_screen_manager.add_widget(HomeworkScreen(name='HomeworkScreen'))
        globals.screen.ids.homework_screen_manager.add_widget(HomeworkDetailsScreen(name='HomeworkDetailsScreen'))

        globals.screen.ids.homework_button.bind(on_tab_press=display_homework_tiles.display_hw)

        return globals.screen


    def on_start(self):
        self.fps_monitor_start()

        #Begin initial loading/generation

        globals.API_CLIENT = StudentClient("********", (0,0,0))

        globals.API_CLIENT.login()


    #self.screen.ids.homework_scroll.rows += 1


if __name__ == "__main__":  
    MainApp().run()