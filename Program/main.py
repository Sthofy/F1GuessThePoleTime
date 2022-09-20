import os

cwd = os.getcwd()
os.environ['KIVY_HOME'] = cwd + '/conf'

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from LoginPage import LoginWidget
from MainPage import MainWidget


class Main(MDApp):
    def __init__(self, **kwargs):
        self.title = "My Material Application"
        super().__init__(**kwargs)

    def build(self):
        self.root = Builder.load_file('KV-files/root.kv')

        screens = [LoginWidget(name="login"), MainWidget(name='main')]
        sm = ScreenManager()

        for screen in screens:
            sm.add_widget(screen)
        sm.current = "login"
        return sm


if __name__ == '__main__':
    Main().run()
