from kivy.uix.screenmanager import Screen
import DB_Manager
import bcrypt


class Login(Screen):
    def show_hide_pw(self):
        if self.ids['login_password'].password:
            self.ids['show_hide_btn'].icon = 'eye'
            self.ids['login_password'].password = False
        else:
            self.ids['show_hide_btn'].icon = 'eye-off'
            self.ids['login_password'].password = True

    def login(self):
        try:
            username = self.ids['login_username'].text
            curr_password = self.ids['login_password'].text

            req = DB_Manager.login_user(username)
            pw_hash = req[0]["password"]

            if bcrypt.checkpw(bytes(curr_password, encoding='utf-8'), pw_hash):
                self.manager.current = 'home'
                self.manager.ids.home.logged_in_user = (req[0]["id"])

        except Exception as e:
            print(e)
