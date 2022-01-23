import globals

def display_activity(*args):
    globals.CURRENT_TAB = "activity"
    globals.screen.ids.toolbar.title = "Activity"