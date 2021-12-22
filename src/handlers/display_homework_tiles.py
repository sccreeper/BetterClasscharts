from datetime import date, datetime
from util import DAY, MONTH, _Date, friendly_date
import time as t
from handlers.display_homework_details import display_homework_details

import globals


def display_hw(*args):
    time = datetime.now()

    data = globals.API_CLIENT.get_homework()

    globals.screen.ids.toolbar.title = "Homework" #Switch title

    if len(data) == globals.HOMEWORK_LENGTH:
        return
    else:
        globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data = []

    homework_lists = {
        "turned_in" : [],
        "due" : [],
        "late" : []
    }

    #Sort the homework into turned in, due, and late

    for hw in data:
        
        due_date = hw["due_date"].split("-")
        due_date = date(int(due_date[0]), int(due_date[1]), int(due_date[2]))

        if hw["status"]["ticked"] == "yes": homework_lists["turned_in"].append(hw)
        elif hw["status"]["ticked"] == "no" and t.time() < t.mktime(due_date.timetuple()): homework_lists["due"].append(hw)
        else: homework_lists["late"].append(hw)
    
    globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(
            {
                "viewclass" : "MDLabel",
                "font_style" : "Button",
                "text" : "Turned in",
                "id" : "label_turned_in"
            }
    )

    for L in homework_lists:
        
        _hw_list = homework_lists[L]

        if L == "due":
                globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(
            {
                "viewclass" : "MDLabel",
                "id" : "label_due",
                "font_style" : "Button",
                "text" : "Due"
            }
    )

        for hw in _hw_list:

            due_date = hw["due_date"].split("-")
            due_date = date(int(due_date[0]), int(due_date[1]), int(due_date[2]))

            if due_date.day == time.day + 1:
                due_date_string = "Tommorow"
            else:
                due_date_string = f"{DAY[due_date.weekday()]} {due_date.day}{friendly_date(due_date.day)} {MONTH[due_date.month - 1]} {'' if due_date.year == time.year else due_date.year}"
                
        
            globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(
                {
                    "viewclass" : "HomeworkView",
                    "hw_title" : hw["title"],
                    "hw_subtitle" : hw["subject"] + " - Due: " + due_date_string,
                    "hw_id" : hw["id"]

                }
            )