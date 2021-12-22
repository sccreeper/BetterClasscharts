from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty, NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast

import globals

class HomeworkDetailsView(GridLayout):
    hw_title = StringProperty()
    hw_description = StringProperty()
    
    hw_due = StringProperty()
    hw_set = StringProperty()

    hw_turned_in = BooleanProperty()

    hw_id = NumericProperty()

    def hand_in_hw(self, checkbox, value):
        
        
        #Hand in or 'un hand in' the HW and do toast accordingly

        success = globals.API_CLIENT.hand_in_homework(self.hw_id)

        if success:
            toast("Homework handed in!")
        else:
            toast("There was an error.")




