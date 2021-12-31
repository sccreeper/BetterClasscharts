import kivy
import kivymd
from kivy.lang import Builder
from kivymd.app import MDApp

import sys

sys.path.append("..")

from views.py.login import LoginView

Builder.load_file('../views/kv/login.kv')

class Test(MDApp):
    def build(self):
        screen = LoginView()

        return screen

if __name__ == "__main__":
    Test().run()