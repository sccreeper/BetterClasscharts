from cmath import log
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

from handlers.settings import logout

class SettingsScreen(Screen):

    student_code = StringProperty()

    def logout(self, *args):
        logout()

    pass
