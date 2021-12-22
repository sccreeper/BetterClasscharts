from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.utils import platform

from kivymd.app import MDApp
from api.client import StudentClient

from views.py import homework_view

import globals
from handlers import display_homework_tiles, display_activity, display_timetable, display_homework_details

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

        Window.bind(on_key_up=self.handle_keyup)

        globals.screen = MainScreen()

    def build(self):

        #Init button callbacks, other shit etc.

        #self.theme_cls.theme_style = "Dark"

        globals.screen.ids.homework_screen_manager.add_widget(HomeworkScreen(name='HomeworkScreen'))
        globals.screen.ids.homework_screen_manager.add_widget(HomeworkDetailsScreen(name='HomeworkDetailsScreen'))

        #Bind buttons to update screen
        globals.screen.ids.homework_button.bind(on_tab_press=display_homework_tiles.display_hw)
        globals.screen.ids.activity_button.bind(on_tab_press=display_activity.display_activity)
        globals.screen.ids.timetable_button.bind(on_tab_press=display_timetable.display_timetable)

        return globals.screen


    def on_start(self):
        self.fps_monitor_start()

        #Begin initial loading/generation

        globals.API_CLIENT = StudentClient("********", (0,0,0))

        globals.API_CLIENT.login()
    
    
    def post_build_init(self,ev):
        if platform == 'android':
            import android
            android.map_key(android.KEYCODE_BACK, 1001)

    
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
    MainApp().run()