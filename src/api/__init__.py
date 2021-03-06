# API globals

#URLs
CLASSCHARTS_URL = "https://www.classcharts.com"

#Endpoints

class ENDPOINT:
    CHECKCODE = "/student/checkpupilcode/"
    LOGIN = "/apiv2student/login"
    HW_HAND_IN = "/apiv2student/homeworkticked/"
    ACTIVITY = "/apiv2student/activity/"
    TIMETABLE = "/apiv2student/timetable/"

class SYNC_ENDPOINT:
    PING = "/ping"
    LOGIN = "/login"

HTTP_PROTOCOLS = ["http", "https"]