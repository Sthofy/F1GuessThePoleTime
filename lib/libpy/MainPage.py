from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList

import Models.LoggedInUserModel as LoggedInUser


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class MainWidget(Screen):
    Builder.load_file('../libkv/mainpage.kv')


def create_logged_in_user(data):
    print(data)
    LoggedInUser.uid = data[0]
    LoggedInUser.username = data[1]
    LoggedInUser.email = data[2]
    LoggedInUser.password = data[3]
    LoggedInUser.phone = data[4]
