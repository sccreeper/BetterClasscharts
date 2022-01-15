from dataclasses import dataclass
import mimetypes

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
    "Saturday"
    "Sunday"
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

def friendly_date(date: int) -> str:
    """
    Returns st, nd, rd, or th depending on the int
    """

    if date >= 10 and date <= 20: return "th"
    elif str(date)[len(str(date))-1] == "1": return "st"
    elif str(date)[len(str(date))-1] == "2": return "nd"
    elif str(date)[len(str(date))-1] == "3": return "rd"
    else: return "th"