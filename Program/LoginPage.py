from kivy.uix.screenmanager import Screen
from kivy.lang import Builder


class LoginWidget(Screen):
    Builder.load_file('KV-files/loginpage.kv')
