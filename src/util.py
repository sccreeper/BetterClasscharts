from dataclasses import dataclass
import mimetypes
from datetime import date, datetime

from kivymd.color_definitions import colors
from kivy.utils import get_color_from_hex
from kivy.base import EventLoop
from kivy.utils import platform as kivy_platform

import globals


def read_file(path):
    with open(path, 'r') as file:
        return file.read()

def write_file(path, data):
    with open(path, 'w') as file:
        return file.write(data)

@dataclass
class _Date:
    day: int
    month: int
    year: int

MONTH = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

DAY = [ #Works provided that Monday is 0, Sunday is 6
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

SHORT_DAY = [

    "Mon",
    "Tue",
    "Wed",
    "Thur",
    "Fri",
    "Sat",
    "Sun"

]

#Add extra types to mimetypes module

#Microsoft (Common ones)
mimetypes.add_type("application/msword", ".docx")
mimetypes.add_type("application/vnd.ms-powerpoint", ".pptx")
mimetypes.add_type("application/vnd.ms-excel", ".xlsx")

#Open document From: (https://en.wikipedia.org/wiki/OpenDocument)

mimetypes.add_type("application/vnd.oasis.opendocument.text", "odt")
mimetypes.add_type("application/vnd.oasis.opendocument.presentation", "odp")
mimetypes.add_type("application/vnd.oasis.opendocument.spreadsheet", "ods")

#Dates

def friendly_date(date: int) -> str:
    """
    Returns st, nd, rd, or th depending on the int
    """

    if date >= 10 and date <= 20: return "th"
    elif str(date)[len(str(date))-1] == "1": return "st"
    elif str(date)[len(str(date))-1] == "2": return "nd"
    elif str(date)[len(str(date))-1] == "3": return "rd"
    else: return "th"


def english_date(_date: str, is_due=False) -> str:
    due_date = _date.split("-")
    due_date = date(int(due_date[0]), int(due_date[1]), int(due_date[2]))

    time = datetime.now()

    #Figure out if homework is late
    if is_due and datetime(due_date.year, due_date.month, due_date.day).timestamp() < time.timestamp():
        LATE = True
    else: LATE = False

    if due_date.day == time.day + 1:
        due_date_string = "[color=ff0000]Tommorow [/color]"
    elif due_date.day == time.day:
        due_date_string = "[color=ff0000]Today [/color]" if is_due else "Today"
    elif due_date.day == time.day - 1:
        due_date_string = "[color=ff0000]Yesterday [/color]" if is_due else "Yesterday"
    else:
        due_date_string = f"{'[color=ff0000]' if is_due and LATE else ''}{DAY[due_date.weekday()]} {due_date.day}{friendly_date(due_date.day)} {MONTH[due_date.month - 1]} {'' if due_date.year == time.year else due_date.year}{'[/color]' if is_due and LATE else ''}"

    return due_date_string

#Here because used very widely.
def get_selected_background_colour(is_down):

    if is_down == "down":
        return get_color_from_hex(colors[globals.CURRENT_CONFIG["accent_name"]]["900"]) if globals.CURRENT_CONFIG["dark_mode"] else get_color_from_hex(colors[globals.CURRENT_CONFIG["accent_name"]]["500"])
    else:
        return get_color_from_hex(colors["Gray"]["800"]) if globals.CURRENT_CONFIG["dark_mode"] else get_color_from_hex(colors["Gray"]["400"])

#Easily update the window title.
def set_window_title(title):
    if kivy_platform == "android" or kivy_platform == "ios": #Yes ios isn't supported but future proofing.
        return
    else:
        globals.app_object.set_title(title)