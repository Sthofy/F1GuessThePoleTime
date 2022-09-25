from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
import dataGetter


class TrackList(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        tracks = dataGetter.get_tracks()
        t_keys = list(tracks.keys())
        t_values = list(tracks.values())
        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(tracks),
            column_data=[
                ("N°", dp(30)),
                ("Helyszín", dp(60))],
            row_data=[(f"{t_keys[i]}", f"{t_values[i]}") for i in range(len(t_keys))],
        )
        self.table.add_widget(md_table)


class Schedule(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        schedule_tuple = dataGetter.get_schedule()
        dates = schedule_tuple[0]
        places = schedule_tuple[1]
        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(dates),
            column_data=[
                ("Dátum", dp(30)),
                ("Helyszín", dp(50))],
            row_data=[(f"{dates[i]}", f"{places[i]}") for i in range(len(dates))],
        )
        self.table.add_widget(md_table)


class Standings(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)

        # pos,drivers,teams,points
        standings_tuple = dataGetter.get_driver_standings()
        positions = standings_tuple[0]
        drivers = standings_tuple[1]
        teams = standings_tuple[2]
        points = standings_tuple[3]

        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(positions),
            column_data=[
                ("Helyezés", dp(15)),
                ("Név", dp(30)),
                ("Csapat", dp(30)),
                ("Pont", dp(15))],
            row_data=[(f"{positions[i]}", f"{drivers[i]}", f"@{teams[i]}", f"{points[i]}") for i in
                      range(len(positions))],
        )
        self.table.add_widget(md_table)


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class Home(Screen):
    dialog = None

    def show_track_list(self):
        if not self.dialog:
            content_cls = BoxLayout(orientation='vertical', padding=20, spacing=10)
            tracklist = TrackList()
            btn = MDRaisedButton(text="Close", pos_hint={"center_x": .5})
            content_cls.add_widget(tracklist)
            content_cls.add_widget(btn)
            self.dialog = Popup(
                title="Track List In The Season",
                size_hint=(.9, .9),
                content=content_cls,
            )
            btn.bind(on_release=self.submit)
        self.dialog.open()

    def show_schedule(self):
        if not self.dialog:
            content_cls = BoxLayout(orientation='vertical', padding=20, spacing=10)
            schedule = Schedule()
            btn = MDRaisedButton(text="Close", pos_hint={"center_x": .5})
            content_cls.add_widget(schedule)
            content_cls.add_widget(btn)
            self.dialog = Popup(
                title="Schedule",
                size_hint=(.9, .9),
                content=content_cls,
            )
            btn.bind(on_release=self.submit)
        self.dialog.open()

    def show_standings(self):
        if not self.dialog:
            content_cls = BoxLayout(orientation='vertical', padding=20, spacing=10)
            standings = Standings()
            btn = MDRaisedButton(text="Close", pos_hint={"center_x": .5})
            content_cls.add_widget(standings)
            content_cls.add_widget(btn)
            self.dialog = Popup(
                title="Standings",
                size_hint=(.9, .9),
                content=content_cls,
            )
            btn.bind(on_release=self.submit)
        self.dialog.open()

    def submit(self, *args):
        self.dialog.dismiss(force=True)
        self.dialog = None
