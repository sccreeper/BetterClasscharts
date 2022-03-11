#Kivy imports
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.logger import Logger

#from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivymd.uix.boxlayout import MDBoxLayout

#Other imports
from datetime import datetime, date
from handlers import login_handler

class LoginScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.student_code = StringProperty()
        self.student_dob_year = NumericProperty()
        self.student_dob_month = NumericProperty()
        self.student_dob_day = NumericProperty()


    #Gets the date and sets it to the root properties
    def get_date(self, date: date):
 
        self.student_dob_year = date.year
        self.student_dob_month = date.month
        self.student_dob_day = date.day
    
    def login(self):
        login_handler.login()
    
