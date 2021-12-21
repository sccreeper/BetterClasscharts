from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty
from kivymd.uix.boxlayout import MDBoxLayout

class HomeworkDetailsView(GridLayout):
    hw_title = StringProperty()
    hw_description = StringProperty()
    
    hw_due = StringProperty()
    hw_set = StringProperty()

    hw_turned_in = BooleanProperty()

    hw_id = 0

    def hand_in_hw(*args):
        pass


