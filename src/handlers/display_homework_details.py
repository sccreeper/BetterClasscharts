from kivy.logger import Logger
from kivy.uix.screenmanager import SlideTransition
from views.py.homework_details import HomeworkDetailsView

import globals

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
    #print(globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").ids)

    globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").clear_widgets() #Clear all children

    globals.screen.ids.homework_screen_manager.get_screen("HomeworkDetailsScreen").add_widget(

        HomeworkDetailsView(
            hw_title = hw["title"],
            hw_description = hw["description"].replace("&nbsp;", " "),
            hw_set = "set: " + hw["issue_date"],
            hw_due = "due: " + hw["due_date"],

            hw_turned_in = True if hw["status"]["ticked"] == "yes" else False
        )

    )


    #Transition to homework screen
    globals.screen.ids.homework_screen_manager.transition = SlideTransition(direction="left",duration=0.25)
    globals.screen.ids.homework_screen_manager.current = "HomeworkDetailsScreen"

    #globals.screen.ids.

