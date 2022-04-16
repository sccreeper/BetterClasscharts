from cmath import log
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from handlers.settings import logout, show_about_screen, show_appearance_screen

class SettingsScreen(Screen):

    student_code = StringProperty()
    student_name = StringProperty()

    def logout(self, *args):
        logout()
    def about_screen(self, *args):
        show_about_screen()
    def show_appearance_screen(self, *args):
        show_appearance_screen()
    

