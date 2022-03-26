from datetime import timedelta
from handlers.display_timetable import display_timetable

from kivymd.uix.boxlayout import MDBoxLayout

import globals
class Timetable(MDBoxLayout):

    def date_left(*args):
        globals.START_DAY -= timedelta(days=5)
        display_timetable()


    def date_right(*args):
        globals.START_DAY += timedelta(days=5)
        display_timetable()