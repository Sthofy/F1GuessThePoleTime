import os

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from LoginPage import LoginWidget
from MainPage import MainWidget

sm = ScreenManager()


class Main(MDApp):

    def change_screen(self, screen):
        sm.current = screen

    def __init__(self, **kwargs):
        self.title = "F1 Guess The Pole Time"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file('KV-files/root.kv')

        screens = [LoginWidget(name="login"), MainWidget(name='main')]

        for screen in screens:
            sm.add_widget(screen)
        sm.current = "login"
        return sm


if __name__ == '__main__':
    Main().run()
