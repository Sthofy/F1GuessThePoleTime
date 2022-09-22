from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import DB_Manager


class RegisterWidget(Screen):
    Builder.load_file('KV-files/registerpage.kv')

    def get_data(self):
        username = self.ids.register_username.text
        email = self.ids.register_email.text
        password = self.ids.register_password.text
        phone = self.ids.register_phone.text

        is_success = DB_Manager.register_user(username, email, password, phone)

        if is_success:
            self.parent.current = 'login'

    def back_to_login(self):
        for cont in self.ids:
            self.ids[cont].text = ''
        self.parent.current = 'login'
