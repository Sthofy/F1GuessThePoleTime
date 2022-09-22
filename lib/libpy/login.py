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
            hash = req[0]["password"]

            self.manager.current = "home"
            # if bcrypt.checkpw(bytes(curr_password, encodings='utf-8'), hash):
            #     self.manager.current='home'

        except Exception as e:
            print(e)
