from kivy.metrics import dp
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.list import MDList
from kivymd.uix.menu import MDDropdownMenu
import DB_Manager
import user_score_helper


class TrackList(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = DB_Manager.get_all_tracks()

        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(data),
            column_data=[
                ("N°", dp(30)),
                ("Helyszín", dp(60))],
            row_data=[(f"{i + 1}", f"{data[i][0]}") for i in range(len(data))],
        )
        self.table.add_widget(md_table)


class Schedule(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        schedule = DB_Manager.get_all_tracks()

        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(schedule),
            column_data=[
                ("Dátum", dp(40)),
                ("Helyszín", dp(50))],
            row_data=[(f"{schedule[i][1]}", f"{schedule[i][0]}") for i in range(len(schedule))],
        )
        self.table.add_widget(md_table)


class Standings(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # pos,drivers,points
        driver_standings = DB_Manager.get_driver_standings()

        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(driver_standings),
            column_data=[
                ("Helyezés", dp(25)),
                ("Név", dp(30)),
                ("Pont", dp(25))],
            row_data=[(f"{driver_standings[i][0]}", f"{driver_standings[i][1]}", f"{driver_standings[i][2]}") for i in
                      range(len(driver_standings))],
        )
        self.table.add_widget(md_table)


class Guess(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        drivers = DB_Manager.get_drivers_long_name()
        circuits = DB_Manager.get_circuit_names()

        circuits_drop = [
            {
                "viewclass": "IconListItem",
                "text": f"{circuits[i]}",
                "height": dp(56),
                "on_release": lambda x=circuits[i]: self.set_circuit(x),
            } for i in range(len(circuits))]

        drivers_drop = [
            {
                "viewclass": "IconListItem",
                "text": f"{drivers[i]}",
                "height": dp(56),
                "on_release": lambda x=drivers[i]: self.set_driver(x),
            } for i in range(len(drivers))]

        self.circuit_menu = MDDropdownMenu(
            caller=self.ids.drop_circuit,
            items=circuits_drop,
            position="center",
            width_mult=4,
        )

        self.driver_menu = MDDropdownMenu(
            caller=self.ids.drop_driver,
            items=drivers_drop,
            position="center",
            width_mult=4,
        )
        self.driver_menu.bind()
        self.circuit_menu.bind()

    def set_circuit(self, text_item):
        self.ids.drop_circuit.set_item(text_item)
        self.circuit_menu.dismiss()

    def set_driver(self, text_item):
        self.ids.drop_driver.set_item(text_item)
        self.driver_menu.dismiss()


class Scoreboard(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = DB_Manager.get_user_standings()

        self.table = self.ids.table
        md_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.55},
            size_hint=(0.9, 0.8),
            rows_num=len(data),
            column_data=[
                ("N°", dp(10)),
                ("Username", dp(35)),
                ("Score", dp(35))],
            row_data=[(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}") for i in range(len(data))],
        )
        self.table.add_widget(md_table)


class IconListItem(OneLineIconListItem):
    pass


class ContentNavigationDrawer(BoxLayout):
    pass


class DrawerList(ThemableBehavior, MDList):
    pass


class Home(Screen):
    dialog = None
    logged_in_user = -1

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

    def show_guess(self):
        if not self.dialog:
            content_cls = Guess()
            self.dialog = MDDialog(
                title="Who will win the Qualification?",
                type="custom",
                content_cls=content_cls,
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        on_release=self.submit
                    ),
                    MDRaisedButton(
                        text="Guess",
                        on_release=lambda x: self.save_guess(content_cls)
                    ),
                ],
            )
        self.dialog.open()

    def show_scoreboard(self):
        if not self.dialog:
            content_cls = BoxLayout(orientation='vertical', padding=20, spacing=10)
            scoreboard = Scoreboard()
            btn = MDRaisedButton(text="Close", pos_hint={"center_x": .5})
            content_cls.add_widget(scoreboard)
            content_cls.add_widget(btn)
            self.dialog = Popup(
                title="LEADERBOARD",
                size_hint=(.9, .9),
                content=content_cls,
            )
            btn.bind(on_release=self.submit)
        self.dialog.open()

    def save_guess(self, form):
        driver = form.ids.drop_driver.current_item
        circuit = form.ids.drop_circuit.current_item
        time = " " + form.ids.guess_time.text

        guess = (driver, circuit, time, self.logged_in_user)
        DB_Manager.insert_guess(guess)

        self.save_score(guess)

        self.submit()

    def save_score(self, data):
        score = user_score_helper.calculate_score(data)
        DB_Manager.update_user_score((self.logged_in_user, score))

    def submit(self, *args):
        self.dialog.dismiss(force=True)
        self.dialog = None
