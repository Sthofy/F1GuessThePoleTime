# **Suhajda Kirstóf - IMVC5O**

Egy C# nyelven írt hobbi projektem alap átirata pythonban.
Fő feladata, hogy megtippeljük milyen idővel és ki fogja megnyerni az adott versenyhétvége időmérőjét.
(A magyar közvetítés kommentátora találta ki a játékot miszerint megosztja saját oldalán az ő tippjét a nézők pedig kommentben)
A fő gondolatot tovább gondolva került bele felsználó kezelés, pár információ világbajnoskág állásáról,egy rangsor a felhasználókról
(tippek pontossága után pontok járnak) stb.

Fontos megjegyezni, hogy a program nincs kész csak felületes átirata a C# projektnek.
Nem tartalmaz vagy csak nyomokban kivételkezelést, a felhasználó által megadott adatok ellenőrzését.

## A műkődésének technikai oldala
  - Adatbázis kezelés: SQLite adatbázit használ ami lokálisan tárolja az datokat így nem szükséges adatbázis tárhelyet bérelni.
   Nem kell API-t írni mert nem távoli eléréssek jut az adatokhoz. (A felhasználói rangsorhoz ez alkalmatlan mivel csak a bejelentkezett felhaszmnálókat tárolja)
  
  - Web Scrap: A web scrapping egy szürkezónás megoldás mivel folyamatos hívásokat végez a cél weboldalra. Sok hívás megfelelne egy túlterheléses támadásnak.
   Mivel nincs saját adatom és nem végez túl sok hívást a program így használható. Az adatok az M4Sport.hu/Boxutca oldalról származnak.
   
  - Felhasználói felület: Kivy és KiviMD-t használtam mert jobbnak találtam a Tkinter-nél. Kivy szolgáltatja az alapot a KivyMD pedig egy közösségi megoldás
   ami implementálja a Google Material Desing-t.
   
   
## Felhasznált csomagok:
  A szükséges interperter 3.7+
  - Kivy
  - Kivymd
  - bcrypt
  - beautifulsoup4
  
### Felhasznált Modulok:
  - bcript
  - sqlite3
  - datetime
  - requests
  - bs4 (BeutifulSoup4)
  - kivy/kivymd (túl sok modul pl Screen,BoxLayout stb)
  - os
  - time
  - sys
  - stb....
### Saját modulok:
  - DB_Manager
  - dataGette
  - user_score_helper
  - home
  - login
  - manager
  - profile
  - register
  
### Saját függvények:
#### home:
    - load_screen
    - set_circuit
    - set_driver
    - show_track_list
    - show_schedule
    - show_standings
    - show_guess
    - show_scoreboard
    - save_guess
    - save_score
    - submit
#### login
    - show_hide_pw
    - login
#### manager:
    - change_screen
#### profile:
    - show_username
    - show_email
    - show_password
    - show_delete
    - change
#### register:
    - get_data
#### dataGetter:
    - set_soup
    - get_driver_standings
    - get_schedule
    - get_drivers
    - get_teams_standing
    - get_qualification_results
    - get_circuit_name
    - get_driver_related_data
#### user_score_helper:
    - load_previous_score
    - load_correct_time
    - load_correct_driver
    - time_convert
    - calculate_score
#### DBManager:
    - perform_select
    - register_user
    - login_user
    - update_user
    - insert_tracks
    - date_parser
    - insert_team_standings
    - insert_driver_standings
    - insert_drivers
    - insert_qualifications_results
    - get_driver_id
    - get_circuit_id
    - load_data_from_web
    - get_all_tracks
    - get_driver_standings
    - get_drivers_long_name
    - get_driver_name
    - get_circuit_names
    - get_driver_id_from_result
    - insert_guess
    - get_qualification_id
    - get_user_score
    - get_qualification_time
    - update_user_score
    - get_user_from_score
    - insert_first_score
    - get_username
    - get_user_standings
