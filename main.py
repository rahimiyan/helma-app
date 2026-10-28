import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

kivy.require("2.3.0")

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=40, spacing=20)
        label = Label(text="Esmaeel_Rahimiyan", font_size="32sp", bold=True, color=get_color_from_hex("#FFFFFF"), halign="center", valign="middle")
        layout.add_widget(label)
        self.add_widget(layout)
        Clock.schedule_once(self.go_home, 5.0)
    def go_home(self, dt):
        self.manager.current = "home"

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=40, spacing=10)
        layout.add_widget(Label(text="خوش آمدید", font_size="28sp", color=get_color_from_hex("#000000")))
        layout.add_widget(Label(text="Esmaeel_Rahimiyan", font_size="18sp", color=get_color_from_hex("#333333")))
        self.add_widget(layout)

class HelmaApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex("#1E88E5")
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    HelmaApp().run()
