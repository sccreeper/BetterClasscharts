from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineAvatarIconListItem
from kivy.properties import StringProperty, ColorProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

import globals

class ActivityScreen(Screen):
    pass

class CustomThreeLineAvatarIconListItem(ThreeLineAvatarIconListItem):
    icon = StringProperty()
    icon_color = ColorProperty()
    description_text = StringProperty()
    dialog = None

    def on_release(self):

        self.dialog = MDDialog(

            title="Note",
            text=self.description_text,
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    text_color=globals.app_object.theme_cls.primary_color,
                    on_release=lambda x: self.close_dialog()
                )
            ]

        )

        self.dialog.open()
    
    def close_dialog(self):
        self.dialog.dismiss(force=True)
