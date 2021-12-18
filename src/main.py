from kivy.lang import Builder

from kivymd.app import MDApp


class Test(MDApp):

    def build(self):
        self.theme_cls.material_style = "M3"
        return Builder.load_string(
            '''
#:import get_color_from_hex kivy.utils.get_color_from_hex


MDScreen:

    MDBottomNavigation:
        panel_color: get_color_from_hex("#eeeaea")
        selected_color_background: get_color_from_hex("#97ecf8")
        text_color_active: 0, 0, 0, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Activity'
            icon: 'bell'

            MDLabel:
                text: 'No Activity'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Homework'
            icon: 'bookshelf'

            MDLabel:
                text: 'Discord'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Timetable'
            icon: 'calendar'

            MDLabel:
                text: 'LinkedIN'
                halign: 'center'
'''
        )


Test().run()