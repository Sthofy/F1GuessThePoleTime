from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    def change_screen(self, screen):
        self.current = screen
