from datetime import date, datetime
from re import T
from util import DAY, MONTH, _Date, english_date, friendly_date
import time as t

from handlers.display_homework_details import display_homework_details
from views.py import homework_sorter

from kivy.logger import Logger

import globals


def display_hw(*args):

    globals.CURRENT_TAB = "homework"
    
    #Semi-globals
    time = datetime.now()

    IS_THERE_TURNED_IN = True
    IS_THERE_DUE = True
    NO_HW = False

    SHOWING_DUE = False
    SHOWING_HANDED_IN = True

    data = globals.API_CLIENT.get_homework()

    #Start of proc

    Logger.info(f"Application: Recieved homework object. Length - {len(data)}")
    
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
    
    #See wether to show turned in or due.
    if len(homework_lists["turned_in"]) == 0:
        IS_THERE_TURNED_IN = False
    
    if len(homework_lists["due"] + homework_lists["late"]) == 0:
        IS_THERE_DUE = False

    if not IS_THERE_DUE and not IS_THERE_TURNED_IN:
        NO_HW = True

    
    if not NO_HW:
    
        if IS_THERE_TURNED_IN: 
        
            globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(
                    {
                        "viewclass" : "HomeworkSorter",
                        "hidden" : globals.SHOW_HANDED_IN,
                        "text" : "Turned in",
                    }
            )

        for L in homework_lists:
            
            _hw_list = homework_lists[L]

            if L == "due":
                globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(
                    {
                        "viewclass" : "HomeworkSorter",
                        "hidden" : globals.SHOW_DUE,
                        "text" : "Due"
                    }

                )

                SHOWING_DUE = True
                SHOWING_HANDED_IN = False
            

            for hw in _hw_list:

                if SHOWING_DUE and not globals.SHOW_DUE:
                    continue
                elif SHOWING_HANDED_IN and not globals.SHOW_HANDED_IN:
                    continue

                due_date_string = english_date(hw["due_date"], is_due=True if SHOWING_DUE else False)
                
                globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(
                    {
                        "viewclass" : "HomeworkView",
                        "hw_title" : hw["title"],
                        "hw_subtitle" : hw["subject"] + " - Due: " + due_date_string,
                        "hw_id" : hw["id"]

                    }
                )
    #If there is no homework, show alternative message
    else:
        globals.screen.ids.homework_screen_manager.get_screen("HomeworkScreen").ids.homework_scroll.data.append(       
            {
                "viewclass" : "MDLabel",
                "font_style" : "H5",
                "halign" : "center",
                "text" : "No homework!"
            }
        )
