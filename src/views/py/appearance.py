from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.dropdownitem import MDDropDownItem
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.selectioncontrol import MDCheckbox

from kivy.properties import StringProperty, ListProperty, ColorProperty
from kivy.metrics import dp

from handlers.settings import change_theme_colour, change_dark_mode
import globals

class AppearanceScreen(Screen):
    def go_back(*args):
        
        #Transition
        
        globals.screen_manager.transition = SlideTransition(direction="right", duration=0.25)
        globals.screen_manager.current = "SettingsScreen"


class ThemeCheckComponent(MDGridLayout): text = StringProperty()

class ThemeCheck(MDCheckbox):

    def change_theme_colour(self, caller):
        if caller == "UI":
            change_dark_mode()

class ColourPickerDropdown(MDDropDownItem):
    menu_items = ListProperty()
    current_colour = StringProperty()
    menu = None

    def on_release(self):

        menu_items = []

        for colour in globals.ACCENT_COLOURS:

            menu_items.append(
                {
                    "viewclass": "OneLineListItem",
                    "text": colour[0],
                    "height": dp(56),
                    "on_release": lambda x=colour: self.change_item(x[0], x[1]),
                    "theme_text_color": "Custom",
                    "text_color": colour[1]
                }

            )

        self.menu = MDDropdownMenu(
            caller=globals.appearance_screen.ids.colour_picker,
            items=menu_items,
            width_mult=2,
        )
        
        self.menu.bind()

        self.menu.open()

    def change_item(self, text, hex):

        self.current_colour = text

        change_theme_colour(hex, text)

        self.menu.dismiss()



