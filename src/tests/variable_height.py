from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):
    def build(self):
        root = FloatLayout()

        b = GridLayout(
            cols=1,
            pos_hint={
                'center_x': .5,
                'center_y': .5},
            size_hint=(None, None),
            spacing=20,
            width=200)
        b.bind(minimum_height=b.setter('height'))
        root.add_widget(b)

        for text_length in range(0, 80, 20):
            l = Label(
                text='word ' * text_length,
                size_hint_y=None)
            l.bind(width=lambda s, w:
                   s.setter('text_size')(s, (w, None)))
            l.bind(texture_size=l.setter('size'))
            b.add_widget(l)

        return root


if __name__ == '__main__':
    MyApp().run()