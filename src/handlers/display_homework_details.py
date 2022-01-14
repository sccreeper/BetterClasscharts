from kivy.logger import Logger
from kivy.uix.screenmanager import SlideTransition
from views.py.homework_details import HomeworkDetailsView

from handlers.desc_parser import Parser

import globals
from handlers import open_url

def display_homework_details(*args):
    Logger.info(f"Application: Displaying homework {args[0]}")

    #Get homework data

    hw_data = globals.API_CLIENT.get_homework()
    
    #SELECT * FROM hw WHERE id = args[0]
    for hw in hw_data:
        if hw["id"] == args[0]:
            hw_data = hw
            break
        else: continue
    
    #Set data

    hw_status_id = hw["status"]["id"]

    #print(globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").ids)

    #Set widgets on screen

    globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").clear_widgets() #Clear all children

    globals.screen.ids.toolbar.left_action_items = [["arrow-left", go_back]]

    #Format description
    
    #Replace pointless newlines at beginning of hw desc
    
    hw_description = hw["description"].replace("&nbsp;", " ")

    index = 0

    for c in hw_description:

        if c == "\n":
            temp = list(hw_description)
            temp[index] = ""

            hw_description = ''.join(temp)

        else:
            break
    
    desc_parsed = Parser()
    hw_description = desc_parsed.parse(hw_description)


    globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").add_widget(

        HomeworkDetailsView(
            hw_title = hw["title"],
            
            hw_description = hw_description,
            desc_size_hint = (1.0, 1.0),

            hw_set = "set: " + hw["issue_date"],
            hw_due = "due: " + hw["due_date"],

            hw_turned_in = True if hw["status"]["ticked"] == "yes" else False,

            hw_id = hw_status_id
        )

    )

    
    #Transition to homework screen
    globals.screen.ids.homework_screen_manager.transition = SlideTransition(direction="left",duration=0.25)
    globals.screen.ids.homework_screen_manager.current = "HomeworkDetailsScreen"

    #Bind ref
    # print(globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").ids)
    # globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").ids.hw_desc.bind(on_ref_press=open_url.launch_webbrowser)

    #globals.screen.ids.

#Logic for back arrow

def go_back(*args):

    #Clear menu
    globals.screen.ids.toolbar.left_action_items = []
    
    #Switch back to main screen
    globals.screen.ids.homework_screen_manager.transition = SlideTransition(direction="right",duration=0.25)
    globals.screen.ids.homework_screen_manager.current = "HomeworkScreen"
