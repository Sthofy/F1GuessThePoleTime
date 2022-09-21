from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import DB_Manager


class LoginWidget(Screen):
    Builder.load_file('KV-files/loginpage.kv')

    logged_in_user = ''

    def get_logged_in_user(self):
        return self.logged_in_user

    def login(self):
        username = self.ids.login_username.text
        password = self.ids.login_password.text
        logged_in_user = DB_Manager.login_user(username, password)

        if (logged_in_user.uid != None):
            self.parent.current = 'main'
