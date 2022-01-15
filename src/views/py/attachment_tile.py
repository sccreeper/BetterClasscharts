from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import CircularRippleBehavior

from handlers.open_file import open_file


class AttachmentTile(CircularRippleBehavior, ButtonBehavior, BoxLayout):
    attachment_name = StringProperty()
    attachment_icon = StringProperty()

    download_progress = NumericProperty()

    attachment_url = StringProperty()

    homework_id = NumericProperty()

    #Referenced by layout in kv file
    def view_attachment(self):
        open_file(self, self.attachment_url, self.homework_id, self.attachment_name)
