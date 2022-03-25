from datetime import date
from tkinter import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, StringProperty, ColorProperty, NumericProperty

from kivy.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors

from handlers.display_timetable import display_tt_date
import globals
from util import get_selected_background_colour


class DayTile(ButtonBehavior, AnchorLayout):
    selected = BooleanProperty()
    date: date
    display_day = StringProperty()
    background_colour = ColorProperty()
    day_index = NumericProperty()


    def on_press(self):

        #Update other widgets
        for child in globals.screen.ids.timetable.ids.date_buttons.children:
            child.selected = False
            child.background_colour = get_selected_background_colour(self)

        #Update self
        self.selected = True
        self.background_colour = get_selected_background_colour(self)

        display_tt_date(self.day_index)
