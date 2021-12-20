from dataclasses import dataclass

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

def friendly_date(date: int) -> str:
    """
    Returns st, nd, rd, or th depending on the int
    """

    if str(date)[len(str(date))-1] == "1": return "st"
    elif str(date)[len(str(date))-1] == "2": return "nd"
    elif str(date)[len(str(date))-1] == "3": return "rd"
    else: return "th"