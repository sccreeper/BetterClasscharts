from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from handlers.settings import logout, show_about_screen, show_appearance_screen, show_dev_settings

class SettingsScreen(Screen):

    student_code = StringProperty()
    student_name = StringProperty()

    def logout(self, *args):
        logout()
    def about_screen(self, *args):
        show_about_screen()
    def show_appearance_screen(self, *args):
        show_appearance_screen()
    def show_dev_settings(self, *args):
        show_dev_settings()
    