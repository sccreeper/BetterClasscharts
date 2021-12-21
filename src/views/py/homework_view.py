from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior

class HomeworkView(CircularRippleBehavior, ButtonBehavior, BoxLayout):
    hw_title = StringProperty()
    hw_subtitle = StringProperty()

    hw_id = NumericProperty()
