from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivy.properties import StringProperty, ColorProperty

class ActivityScreen(Screen):
    pass

class CustomThreeLineAvatarIconListItem(ThreeLineAvatarIconListItem):
    icon = StringProperty()
    icon_color = ColorProperty()