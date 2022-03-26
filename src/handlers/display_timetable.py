import globals
from datetime import timedelta
from datetime import datetime, date
from threading import Thread
from functools import partial

from kivymd.uix.label import MDLabel
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.metrics import dp

from kivy.clock import Clock


from views.py.timetable.lesson_tile import LessonTile
from util import get_selected_background_colour, SHORT_DAY

def display_timetable(*args):
    globals.CURRENT_TAB = "timetable"
    globals.screen.ids.toolbar.title = "Timetable"

    #Update on top row

    current_day = globals.START_DAY
    d = 0

    for child in reversed(globals.screen.ids.timetable.ids.date_buttons.children):

        child.display_day = f"{current_day.day}\n{SHORT_DAY[current_day.weekday()]}"
        child.background_normal = get_selected_background_colour("normal")
        child.background_down = get_selected_background_colour("down")
        child.date = current_day
        child.day_index = d

        current_day += timedelta(days=1)
        d += 1

    #Force the update of the background.
    for child in globals.screen.ids.timetable.ids.date_buttons.children:
        child.state = "down"
    
    #Show spinner and spawn thread.

    globals.screen.ids.timetable.ids.lesson_list.clear_widgets()
    
    globals.screen.ids.timetable.ids.lesson_list.add_widget(
        MDFloatLayout()
    )

    globals.screen.ids.timetable.ids.lesson_list.children[0].add_widget(

        MDSpinner(
            size_hint=(None, None),
            size=(dp(46), dp(46)),
            pos_hint={'center_x': .5, 'center_y': .5},
            active=True
        )

    )

    Thread(target=get_api_data).start()
    

def get_api_data(*args):
    #Get data from API
    timetable = globals.API_CLIENT.get_timetable(date_range=(globals.START_DAY, globals.START_DAY + timedelta(days=5)))
    globals.TIMETABLE_CACHE = timetable

    Clock.schedule_once(partial(display_tt_date, 0), 0)

def display_tt_date(day_index, *args):
    if globals.TIMETABLE_CACHE == None: return

    #Clear children
    globals.screen.ids.timetable.ids.lesson_list.clear_widgets()

    #Update widgets to display on the screen.

    if len(globals.TIMETABLE_CACHE[day_index]) != 0:

        for lesson in globals.TIMETABLE_CACHE[day_index]:
            globals.screen.ids.timetable.ids.lesson_list.add_widget(

                LessonTile(

                    lesson_name=lesson["subject_name"],
                    lesson_time=f"{lesson['start_time'][11:19]} - {lesson['end_time'][11:19]}", #10:17 - splice the time from the full UTC string.
                    lesson_third_line=f"{lesson['teacher_name']} | {lesson['room_name']}"

                )

        )
    
    else:
        globals.screen.ids.timetable.ids.lesson_list.add_widget(

            MDLabel(
                text="No Lessons!",
                font_style="H5",
                halign="center",
            )

        )