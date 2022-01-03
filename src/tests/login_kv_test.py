import kivy
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp

import sys

sys.path.append("..")

from views.py.login import LoginScreen

Builder.load_file('../views/kv/login.kv')

class Test(MDApp):
    def build(self):
        screen = LoginScreen()

        return screen

if __name__ == "__main__":
    Test().run()