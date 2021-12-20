from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivymd.uix.boxlayout import MDBoxLayout

class HomeworkView(BoxLayout):
    hw_title = StringProperty()
    hw_subtitle = StringProperty()

