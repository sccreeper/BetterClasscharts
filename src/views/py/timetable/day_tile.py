from tkinter import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, StringProperty

from kivy.uix.anchorlayout import AnchorLayout

from handlers.display_timetable import display_tt_date


class DayTile(ButtonBehavior, AnchorLayout):
    selected = BooleanProperty()
    date = StringProperty()
    display_day = StringProperty()

    def on_press(self):
        display_tt_date(self.date)
