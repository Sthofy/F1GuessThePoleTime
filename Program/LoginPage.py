from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

import DB_Manager
import MainPage as Main


class LoginWidget(Screen):
    Builder.load_file('KV-files/loginpage.kv')

    def show_hide_pw(self):
        if self.ids['login_password'].password:
            self.ids['show_hide_btn'].icon = 'eye'
            self.ids['login_password'].password = False
        else:
            self.ids['show_hide_btn'].icon = 'eye-off'
            self.ids['login_password'].password = True

    def login(self):
        username = self.ids.login_username.text
        password = self.ids.login_password.text
        line = DB_Manager.login_user(username, password)

        if line:
            Main.create_logged_in_user(line)
            self.parent.current = 'main'
        else:
            print('No')
