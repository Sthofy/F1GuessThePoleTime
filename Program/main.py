from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from LoginPage import LoginWidget


class WindowManager(ScreenManager):
    pass


class Main(App):
    def build(self):
        self.sm = WindowManager()

        screens = [LoginWidget(name="reviews")]
        for screen in screens:
            self.sm.add_widget(screen)

        self.sm.current = "reviews"
        return self.sm


Main().run()
