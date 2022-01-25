from views.py.activity import CustomThreeLineAvatarIconListItem
from kivy.logger import Logger
import globals
from datetime import datetime, date

TIMES_SWITCHED = 0

def display_activity(*args):

    globals.CURRENT_TAB = "activity"
    globals.screen.ids.toolbar.title = "Activity"

    activity_data = globals.API_CLIENT.get_activity()

    Logger.info(f"Application: Displaying {len(activity_data)} activity item(s)")

    #Clear children so we don't have duplicated data
    globals.screen.ids.activity_screen.ids.activity_list.clear_widgets()

    #Display data
    for data in activity_data:
        
        award_date = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S")

        globals.screen.ids.activity_screen.ids.activity_list.add_widget(
            
            CustomThreeLineAvatarIconListItem(
                text=data["reason"],
                secondary_text=f"{data['score']} point{'s' if data['score'] != 1 else ''}",
                tertiary_text=f"Awarded by {data['teacher_name']} in {data['lesson_name']} on {award_date.day}/{award_date.month}", #TODO make this look nice
                icon="thumb-up" if data["polarity"] == "positive" else "thumb-down",
                icon_color="00FF00" if data["polarity"] == "positive" else "FF0000"

            )

        )