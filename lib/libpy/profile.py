from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class Profile(Screen):
    def show_custom_bottom_sheet(self, sheet):
        bsheet = Factory.PhoneSheet()

        bsheet.ids.btn.on_release = self.printName()

        print(bsheet.ids.btn.on_release)
        if sheet == 'Username':
            self.custom_sheet = MDCustomBottomSheet(screen=Factory.UsernameSheet())
        elif sheet == "Email":
            self.custom_sheet = MDCustomBottomSheet(screen=Factory.EmailSheet())
        elif sheet == "Password":
            self.custom_sheet = MDCustomBottomSheet(screen=Factory.PasswordSheet())
        elif sheet == "Phone":
            self.custom_sheet = MDCustomBottomSheet(screen=bsheet)

        self.custom_sheet.open()

    def printName(self):
        print("hello")
