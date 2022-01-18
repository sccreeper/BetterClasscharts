#Thing used for seperating hw.
#(Turned in, Not turned in etc.)

#Python implementation of src/views/kv/homework_sorter.kv

from kivy.uix.gridlayout import GridLayout
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty, BooleanProperty

from handlers import display_homework_tiles
import globals

class HomeworkSorter(ButtonBehavior, GridLayout):
    text = StringProperty()
    hidden = BooleanProperty()

    def on_press(self):

        #Flip global booleans
        if self.text == "Due":
            globals.SHOW_DUE = not globals.SHOW_DUE
        else:
            globals.SHOW_HANDED_IN = not globals.SHOW_HANDED_IN

        #Refresh homework view
        display_homework_tiles.display_hw()

