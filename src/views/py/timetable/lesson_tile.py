from kivy.properties import StringProperty
from kivymd.uix.list import ThreeLineListItem


class LessonTile(ThreeLineListItem):
    lesson_time = StringProperty()
    lesson_name = StringProperty()
    lesson_third_line = StringProperty()