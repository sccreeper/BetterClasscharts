from views.py.activity import CustomThreeLineAvatarIconListItem
from kivy.logger import Logger
import globals

TIMES_SWITCHED = 0

def display_activity(*args):
    #Very bad practice ik but to fix a bodge in main.py -> MainApp -> on_start
    global TIMES_SWITCHED

    TIMES_SWITCHED += 1

    if TIMES_SWITCHED == 2:
        return

    globals.CURRENT_TAB = "activity"
    globals.screen.ids.toolbar.title = "Activity"

    activity_data = globals.API_CLIENT.get_activity()

    Logger.info(f"Application: Displaying {len(activity_data)} activity item(s)")

    #Clear children so we don't have duplicated data
    globals.screen.ids.activity_screen.ids.activity_list.clear_widgets()

    #Display data
    for data in activity_data:
    
        globals.screen.ids.activity_screen.ids.activity_list.add_widget(
            
            CustomThreeLineAvatarIconListItem(
                text=data["reason"],
                secondary_text=f"{data['score']} point{'s' if data['score'] != 1 else ''}",
                tertiary_text=f"Awarded by {data['teacher_name']} in {data['lesson_name']} on {data['timestamp']}", #TODO make this look nice
                icon="thumb-up" if data["polarity"] == "positive" else "thumb-down",
                icon_color="00FF00" if data["polarity"] == "positive" else "FF0000"

            )

        )