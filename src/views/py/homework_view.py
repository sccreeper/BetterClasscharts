from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from handlers.display_homework_details import display_homework_details

class HomeworkView(CircularRippleBehavior, ButtonBehavior, BoxLayout):
    hw_title = StringProperty()
    hw_subtitle = StringProperty()

    hw_id = NumericProperty()

    def display_hw(self, *args):
        display_homework_details(self.hw_id)
