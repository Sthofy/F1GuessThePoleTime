from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import DB_Manager

DB_Manager.connect()


class RegisterWidget(Screen):
    Builder.load_file('KV-files/registerpage.kv')

    def get_data(self):
        username = self.ids.register_username.text
        email = self.ids.register_email.text
        password = self.ids.register_password.text
        phone = self.ids.register_phone.text
        isSuccess = DB_Manager.register_user(username, email, password, phone)
        if (isSuccess):
            self.parent.current = 'login'
