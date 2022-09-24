import os
from multiprocessing.dummy import Process
from sys import platform
from time import sleep
from kivy import Config
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.app import MDApp

if platform == "win32":
    from os import environ

    environ["KIVY_GL_BACKEND"] = "angle_sdl2"

Config.set("kivy", "exit_on_escape", "0")
Window.size = (600, 800)
Window.softinput_mode = 'below_target'


class F1Guess(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.theme_cls.primary_palette = "Red"
        self.PYTHON_FILES = "lib/libpy"
        self.KIVY_FILES = "lib/libkv"

    def build(self):
        # from kivy import platform
        # if platform == "android":
        #     self.start_service()
        return Builder.load_file("manager.kv")

    def on_start(self):
        Process(target=self.initiate_load_sequence).start()

    def initiate_load_sequence(self):
        # sleep(3)
        self.load_screens()
        Clock.schedule_once(
            lambda x: exec("self.root.ids.manager.add_widget(Factory.Manager())", {"self": self, "Factory": Factory}))
        Clock.schedule_once(
            lambda x: exec("self.root.current = 'manager'", {"self": self}))
        Clock.schedule_once(
            lambda x: exec("self.root.ids.manager.children[0].current = 'profile'", {"self": self}))  # , timeout=2)

    def load_screens(self):
        # -------- import python screens -------- #
        libpy = os.listdir(self.PYTHON_FILES)
        for modules in libpy:
            exec(f"from lib.libpy import {modules.split('.')[0]}")
        # -------------------------------- #

        # ---------- load kivy screens ---------- #
        libkv = os.listdir(self.KIVY_FILES)
        for kv in libkv:
            Builder.load_file(f"{self.KIVY_FILES}/{kv}")
        # --------------------------------------- #

    # def login(self):
    #     User(self).login()


F1Guess().run()
