from kivy.uix.scrollview import ScrollView
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.toast import toast
from kivymd.uix.gridlayout import MDGridLayout

from handlers import open_url, open_image
import globals

class HomeworkDetailsView(MDBoxLayout):
    hw_title = StringProperty()
    
    hw_due = StringProperty()
    hw_set = StringProperty()

    hw_turned_in = BooleanProperty()

    hw_id = NumericProperty()

    desc_size_hint = ListProperty()

    attachment_data = ListProperty()
    hw_description = StringProperty()

    def hand_in_hw(self, checkbox, value):
        
        
        #Hand in or 'un hand in' the HW and do toast accordingly

        success = globals.API_CLIENT.hand_in_homework(self.hw_id)

        if success:
            toast("Homework handed in!")
        else:
            toast("There was an error.")
    
    def open_link(self, _instance, url):
        
        match url[0:3]:
            case "url":
                open_url.launch_webbrowser(url[3:-1])
            case "img":
                open_image.open_image(url)
