from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList

import DB_Manager


class ChangeUsername(BoxLayout):
    pass


class ChangeEmail(BoxLayout):
    pass


class ChangePassword(BoxLayout):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class Profile(Screen):
    dialog = None

    def show_username(self):
        if not self.dialog:
            content_cls = ChangeUsername()
            self.dialog = MDDialog(
                title="Are you want to change your Username?",
                type="custom",
                content_cls=content_cls,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.submit
                    ),
                    MDRaisedButton(
                        text="ACCEPT",
                        on_release=lambda x: self.change(x, content_cls)
                    ),
                ],
            )
        self.dialog.open()

    def show_email(self):
        if not self.dialog:
            content_cls = ChangeEmail()
            self.dialog = MDDialog(
                title="Are you want to change your Email address?",
                type="custom",
                content_cls=content_cls,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.submit
                    ),
                    MDRaisedButton(
                        text="ACCEPT",
                        on_release=lambda x: self.change(x, content_cls)
                    ),
                ],
            )
        self.dialog.open()

    def show_password(self):
        # TODO: check the old_password is equals with current user password
        if not self.dialog:
            content_cls = ChangePassword()
            self.dialog = MDDialog(
                title="Are you want to change your Password?",
                type="custom",
                content_cls=content_cls,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.submit
                    ),
                    MDRaisedButton(
                        text="ACCEPT",
                        on_release=lambda x: self.change(x, content_cls)
                    ),
                ],
            )
        self.dialog.open()

    def show_delete(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Are you sure?",
                text="This will delete your account.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.submit
                    ),
                    MDRaisedButton(
                        text="ACCEPT",
                        on_release=lambda x: self.change(x, "delete")
                    ),
                ],
            )
        self.dialog.open()

    def submit(self, *args):
        self.dialog.dismiss(force=True)
        self.dialog = None

    def change(self, instance_btn, content):
        # TODO: get the logged in user id
        # TODO: check the input fields is not null
        if type(content) is ChangeUsername:
            DB_Manager.update_user("username", content.ids.n_username.text, 2)
        elif type(content) is ChangeEmail:
            DB_Manager.update_user("email", content.ids.n_email.text, 2)
        elif type(content) is ChangePassword:
            DB_Manager.update_user("password", content.ids.new_password.text, 2)
        else:
            DB_Manager.update_user("delete", content, 2)
        self.submit()
