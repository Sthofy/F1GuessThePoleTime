from kivy.uix.screenmanager import Screen
import DB_Manager


class Register(Screen):
    def get_data(self):
        try:
            username = self.ids['register_username'].text
            email = self.ids['register_email'].text
            password = self.ids['register_password'].text

            if DB_Manager.register_user(username, email, password):
                self.manager.current = 'login'
            else:
                print('No')

        except Exception as e:
            print(e)
