from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class MainWidget(Screen):
    Builder.load_file('KV-files/mainpage.kv')
