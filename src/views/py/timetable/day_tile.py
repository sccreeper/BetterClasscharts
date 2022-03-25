from datetime import date
from tkinter import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, StringProperty, ColorProperty

from kivy.uix.anchorlayout import AnchorLayout

from handlers.display_timetable import display_tt_date


class DayTile(ButtonBehavior, AnchorLayout):
    selected = BooleanProperty()
    date: date
    display_day = StringProperty()
    background_colour = ColorProperty()


    def on_press(self):
        display_tt_date(self.date)
