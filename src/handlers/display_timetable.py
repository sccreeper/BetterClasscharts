import globals
from datetime import date, timedelta
from datetime import datetime

from views.py.timetable.lesson_tile import LessonTile

def display_timetable(*args):
    globals.CURRENT_TAB = "timetable"
    globals.screen.ids.toolbar.title = "Timetable"

    #Get data from API
    timetable = globals.API_CLIENT.get_timetable(date_range=(datetime.now(), datetime.now() + timedelta(days=5)))

    #Clear children
    globals.screen.ids.timetable.ids.lesson_list.clear_widgets()

    #Update widgets to display on the screen.
    for lesson in timetable[0]:
        globals.screen.ids.timetable.ids.lesson_list.add_widget(

            LessonTile(

                lesson_name=lesson["subject_name"],
                lesson_time=f"{lesson['start_time'][11:19]} - {lesson['end_time'][11:19]}", #10:17 - splice the time from the full UTC string.
                lesson_third_line=f"{lesson['teacher_name']} | {lesson['room_name']}"

            )

        )


def display_tt_date(current_day, *args):
    pass