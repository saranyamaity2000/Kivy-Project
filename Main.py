from kivy.app import App
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # this above two default constructer line !
        inc = 0.1
        pos = 1
        area = 1
        while area > 0:  # just to test how many buttons fit inside !
            # doesn't matter if i do >0.5 or >1 the total shown is 5 only !
            b = Button(text=str(pos), size_hint=(None, None), size=(dp(100), dp(100)))
            area -= (inc**2)
            if area < 0:
                break
            inc += 0.1
            pos += 1
            self.add_widget(b)


class GridLayoutExample(GridLayout):
    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
