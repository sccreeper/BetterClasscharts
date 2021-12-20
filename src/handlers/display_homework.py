from datetime import date, datetime
from util import MONTH, _Date, friendly_date

import globals


def display_hw(*args):
    time = datetime.now()

    data = globals.API_CLIENT.get_homework()

    for hw in data:

        #Figure out homework due conditions

        #Parse date y/m/d

        due_date = hw["due_date"].split("-")
        due_date = date(int(due_date[0]), int(due_date[1]), int(due_date[2]))

        if due_date.day == time.day + 1:
            due_date_string = "Tommorow"
        else:
            due_date_string = f"{due_date.day}{friendly_date(due_date.day)} {MONTH[due_date.month - 1]} {'' if due_date.year == time.year else due_date.year}"
            
    
        globals.screen.ids.homework_scroll.data.append(
            {
                "viewclass" : "HomeworkView",
                "hw_title" : hw["title"],
                "hw_subtitle" : hw["subject"] + " - Due: " + due_date_string,
            }
        )