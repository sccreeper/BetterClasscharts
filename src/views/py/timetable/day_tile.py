from datetime import date
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, StringProperty, ColorProperty, NumericProperty

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.color_definitions import colors

from handlers.display_timetable import display_tt_date

class DayTile(MDRaisedButton, MDToggleButton):
    date: date
    display_day = StringProperty()
    day_index = NumericProperty()


    def on_state(self, widget, value):

        #Update self
        if value == "down":
            display_tt_date(self.day_index)
