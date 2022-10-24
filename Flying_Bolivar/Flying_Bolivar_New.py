import random
import mysql.connector
from geopy.distance import geodesic
import time
import help
from help import help
from tabulate import tabulate


connection = mysql.connector.connect( # Täytyy vaihtaa username ja password kun testaa koodin toimivuutta.
    host='127.0.0.1',
    port=3306,
    database = 'flight_game',
    user = 'root',
    password = 'Yahoo',
    autocommit = True
    )

import db_iso_country_name_by_continent
def db_iso_country_name_by_continent(continent): # Valitaan country taulusta maan nimi ja iso_country
                                                 # koodi maanosan perusteella.
    sql = f"SELECT DISTINCT iso_country, name from country where continent = '{continent}'"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result


def db_airport_by_country_transport(country, airport_type): # Valitaan airport taulusta nimi ja ident-koodi maan iso_country
                                                            # koodin perusteella ja airport_typen perusteella joka määritellään
                                                            # kulkuvälineen perusteella
    sql = f"SELECT airport.name, airport.ident, airport.type FROM airport, country " \
          f"WHERE country.iso_country = airport.iso_country " \
          f"and airport.iso_country = '{country}' and airport.type in ({airport_type})"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result


def db_airport_continent_iso_country_name_ident_xy_by_ident(ident): # Valitaan airport taulusta nimi, ident,
                                                                    # koordinaatit ident-koodin perusteella
    sql = f"SELECT  country.continent, airport.iso_country, airport.name, airport.ident, latitude_deg, longitude_deg " \
          f"FROM airport, country " \
          f"WHERE airport.iso_country = country.iso_country and ident = '{ident}'"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result


def db_airport_balloonport():
    sql = f"SELECT airport.name, airport.ident, country.continent, airport.iso_country FROM airport, country " \
          f"WHERE country.iso_country = airport.iso_country and airport.type='balloonport'"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result


def select_continent(): # Valitaan maanosa
    if player['Transport']['name'] == 'Kuumailmapallo':
        return
    status = 'in_continentmenu'
    continent_list = ("EU", "AS", "NA", "AF", "AN", "SA", "OC")
    continent_name_list = ('Eurooppa', 'Aasia', 'Pohjois-Amerikka',
                           'Afrikka', 'Etelämanner', 'Etelä-Amerikka', 'Oseania'  )
    continents_n_names = [continent_name_list, continent_list]
    while True:
        print("\n")
        print(tabulate(continents_n_names, headers='firstrow', tablefmt='fancy_grid'))
        continent_selection = input("\nValitse maanosa ISO-koodilla: ").upper()
        if continent_selection.isalpha() and continent_selection in continent_list:
            return continent_selection
        elif continent_selection == 'HELP':
            help(status)
            continue
        else:
            print("\nMaanosaa ei löydy.")
            continue


def select_country(selected_continent): # Valitaan maa
    if player['Transport']['name'] == 'Kuumailmapallo':
        return
    status = 'in_countrymenu'
    while True:
        countries_list = []
        countries = db_iso_country_name_by_continent(selected_continent) # Kutsutaan fuction pelaajan
                                                                         # nykyisen sijainnin maanosan
                                                                         # perusteella
        print("\n")
        print(tabulate(countries, tablefmt='fancy_grid'))
        for i in countries:
            countries_list.append(i[0]) # Lisätään listaan ISO_country koodi
                                        # jotta voidaan tarkistaa onko inputti listassa
        country_selection = input("\nValitse maa: ").upper()
        if country_selection in countries_list:
            return country_selection
        elif country_selection == 'HELP':
            help(status)
            continue
        else:
            print("\nMaata ei löydy.")
            continue


def select_airport_n_fly(selected_country): # Valitaan lentokenttä listasta
    status = "in_airportmenu"
    if player['Transport']['name'] == 'Kuumailmapallo':
        airport = db_airport_balloonport()
        airport_list = []
        print("\n")
        print(tabulate(airport, tablefmt='fancy_grid'))
        for port in airport:
            airport_list.append(port[1])  # Lisätään lentokentän ident listaan tarkistaakseen input.
    else:
        airport_type = airport_type_by_transport(player['Transport']['name']) # Määritetään lentokentän tyyppi pelaajan
                                                                              # nykyisen menopelin perusteella
        airport = db_airport_by_country_transport(selected_country, airport_type)  # Haetaan lentokentät
                                                                                   # nykyisen sijainnin ja
                                                                                   # lentokentän tyypin
                                                                                   # perusteella
        if len(airport) < 1:
            print("\nKyseiselle menopelille ei löytynyt lentokenttää.")
            return
        elif len(airport) > 20:                       # Jos saadaan yli 20 lentokentän lista arvotaan siitä 20kpl.
            airport = random.choices(airport, k=20)

        airport_list = []
        print("\n")
        print(tabulate(airport, tablefmt='fancy_grid'))
        for i in airport:
            airport_list.append(i[1]) # Lisätään lentokentän ident listaan tarkistaakseen input.

    while True:
        airport_selection = input("\nValitse lentokenttä: ").upper()
        if airport_selection in airport_list and airport_selection not in player['Visited']:
            airport = db_airport_continent_iso_country_name_ident_xy_by_ident(airport_selection) # Haetaan tiedot
                                                                                                 # identin perusteella.
            player['Distance'][0] = calculate_distance(player['Current_location'][4], airport_selection)
                                                                                            # Lasketaan kenttien
                                                                                            # välinen etäisyys
            player['Distance'][1] += calculate_distance(player['Current_location'][4], airport_selection) # Kokonais matka
            player['Current_location'][0] = airport[0][0]                                                # Päivitetään pelaajan sijanti tiedot.
            player['Current_location'][1] = airport[0][1]
            weather = random.choice(random_continent_weather())
            player['Current_location'][2] = airport[0][2]
            player['Current_location'][3] = airport[0][3]
            player['Current_location'][4] = (airport[0][4], airport[0][5])
            player['Visited'].append(airport_selection)
            travel_time(player['Distance'], player['Transport'])  # Lasketaan matkaan käytetty aika
            co2_counter(player['Distance'], player['Transport'])  # Lasketaan kulutettu CO2
            if weather not in player['Goals']:
                player['Goals'].append(weather) # Lisätään säätila pelaajan saavutus listaan.
                player['Visited'].append(airport_selection)
                print(f"\n+{'~'*40}+")
                print(f"| Hienoa! Saavutit säätilan: {weather:>11} |")
                print(f"| Matkasi pituus oli: {player['Distance'][0]:>15.0f} km |")
                print(f"| ja se kesti: {player['Travel_time'][0]:>18.1f} tuntia |")
                print(f"| CO2-budjettisi on nyt: {player['CO2_budget']:>15.0f} |")
                print(f"+{'~' * 40}+")
                if len(player['Goals']) == 8 or player['CO2_budget'] == 0:
                    return
                print(f"\nSaavuttamasi säätilat: {' * '.join(player['Goals'])}")
                print("\nSinulta puuttuu vielä:", ', '.join(set(sorted(weather_goals)).difference(set(sorted(player['Goals'])))))
                return
            else:               # Jos kyseisellä kentällä on jo saavutettu säätila.
                if player['CO2_budget'] == 0:
                    return
                else:
                    print(f"\nSää lentokentällä on {weather}. Olet saavuttanut jo kyseisen säätilan. Jatka matkaa.")
                    player['Visited'].append(airport_selection)
                    print(f"\n+{'~'*40}+")
                    print(f"| Matkasi pituus oli: {player['Distance'][0]:>15.0f} km |")
                    print(f"| ja se kesti: {player['Travel_time'][0]:>18.1f} tuntia |")
                    print(f"| CO2-budjettisi on nyt: {player['CO2_budget']:>15.0f} |")
                    print(f"+{'~' * 40}+")
                    print(f"\nSaavuttamasi säätilat: {' * '.join(player['Goals'])}")
                    print("\nSinulta puuttuu vielä:", ', '.join(set(sorted(weather_goals)).difference(set(sorted(player['Goals'])))))
                    return
        elif airport_selection == "HELP":
            help(status)
            continue
        elif airport_selection in player['Visited']:
            print(f"\nOlet jo käynyt täällä.")
            return
        else:
            print("\nLentokenttää ei löydy.")
            continue


def airport_type_by_transport(transport):  # Lentokentän tyyppi määritellään kulkuvälineen perusteella
                                           # ja syötetään SQL koodiin
    if transport == "Hävittäjä":
        airport_type = "'heliport', 'small_airport', 'closed', 'seaplane_base', " \
                       "'balloonport' 'medium_airport', 'large_airport'"
        return airport_type
    elif transport == "Lentokone" or transport == "Liitokone":
        airport_type = "'small_airport', 'closed', 'medium_airport', 'large_airport'"
        return airport_type
    elif transport == "Kuumailmapallo":
        return
    elif transport == "Helikopteri":
        airport_type = "'heliport'"
        return airport_type

# "kuuma", "kylmä", "0-astetta", "10-astetta", "20-astetta", "kirkas", "pilvinen", "tuulinen"
def random_continent_weather():     # Säätila määritellään pelaajan sen hetkisen sijainnin maanosan perusteella
                                    # tehdään vasta kun lentokenttä on valittu
    if 'EU' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [1, 1, 10, 1, 1, 1, 10, 2], k = 75)
        return continent_weather
    elif 'AS' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [10, 0, 1, 2, 2, 10, 2, 1], k = 75)
        return continent_weather
    elif 'NA' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [1, 2, 2, 10, 1, 2, 1, 10], k = 75)
        return continent_weather
    elif 'AF' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [10, 1, 1, 2, 10, 3, 1, 2], k = 75)
        return continent_weather
    elif 'AN' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [0, 10, 0, 0, 0, 2, 2, 2], k = 75)
        return continent_weather
    elif 'SA' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [7, 0, 0, 1, 10, 1, 2, 2], k = 75)
        return continent_weather
    else: #OC
        continent_weather = random.choices(weather_goals, weights = [8, 0, 0, 1, 5, 3, 2, 7], k = 75)
        return continent_weather


def aircrafts(n): # Kulkuväline valikko

    liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50} #määritellään kulkuvälineet ja niiden ominaisuuksia
    lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 275}
    helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 150}
    havittaja = {'name': 'Hävittäjä', 'speed': 1200, 'consumption': 500}
    kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}
    aircraft_list = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo) # Lisätään ne listaan                                                                                   # käyttää sitten niiden indexia
    transport = aircraft_list[n] # Lisätään listan muuttujaan
    print(f"Valitsit: {transport['name']} \nVauhti: {transport['speed']} (km/h) \nKulutus: {transport['consumption']} (CO2)")
    return transport


def transport_valikko():
    status = "in_transportmenu"
    while True:
        print(f"\n{'X---' * 30}X")
        print(f"\nValitse kulkuväline")  # Tulostetaan kulkuvälineen valikko
        print("\n1 - Liitokone \n2 - Lentokone \n3 - Helikopteri \n4 - Hävittäjä \n5 - Kuumailmapallo")
        n = input("\nSyötä kulkuvälineen numero: ").upper() # Kysytään kulkuvälineen valinta
        if n.isdigit():
            n = int(n)
            if 0 < n < 6:
                print("\nGreat!")
                player['Transport'] = aircrafts(n-1) # Päivitetään pelaajan kulkuväline
                return
            else:
                print(f"Vain numerot 1-5 käyvät vastaukseksi.")
                continue
        elif n == 'HELP':
            help(status)
            continue
        else:
            print(f"Vain numerot 1-5 tai help käyvät vastaukseksi.")
            continue





def top10(name, score):  # fuction top10 taulun päivittämiseen (parametrit: pelaajan nimi ja score)
                         # taulun luonti rivi hubin commitissa.
    sql = f"SELECT id, name, score FROM top10 WHERE score in " \
          f"(SELECT min(score) FROM top10) order by id desc"  # Haetaan pienin score ja suurin ID.
    sql2 = f"SELECT * FROM top10"  # Haetaan kaikkien rivien määrä taulusta
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    lowest_score = query_cursor.fetchall()
    query_cursor2 = connection.cursor()
    query_cursor2.execute(sql2)
    query_cursor2.fetchall()
    if query_cursor2.rowcount < 10 and score > 0:
        sql = f"INSERT INTO top10 (name, score) VALUES ('{name}', '{score}')"  # Jos taulussa alle 10 riviä. Lisätään
                                                                               # tuloksia tauluun.
        query_cursor = connection.cursor()
        query_cursor.execute(sql)
        print_top10()
        return
    elif query_cursor2.rowcount == 10 and score > lowest_score[0][2]:  # Kun 10 riviä tulee täyteen päädytään vain
                                                                       # päivittämään taulua
        sql = f"UPDATE top10 SET name = '{name}', score = '{score}' WHERE ID = {lowest_score[0][0]}"
        query_cursor = connection.cursor()
        query_cursor.execute(sql)
        print_top10()
        return
    else:
        return


def print_top10():  # Printataan top10
    sql = f"SELECT * FROM top10 order by score desc"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    top10 = query_cursor.fetchall()
    if query_cursor.rowcount > 0:
        print(f"\nPÄÄSIT TOP10 RAUTAISEEN JOUKKOON!!!")
        print(f"\n+{'-':-<4}+{'-':-<27}+{'-':-<8}+")
        no_in_top10 = 0
        for i in top10:
            no_in_top10 += 1
            print(f"| {no_in_top10:<2} | {i[1]:<25} | {i[2]:>6} |")
        print(f"+{'-':-<4}+{'-':-<27}+{'-':-<8}+")


def main_menu():
    print(f"\nOlet nyt sijainnissa: {', '.join(player['Current_location'][:3])}")
    print(f"Nykyinen kulkuvälineesi on: {player['Transport']['name']}")
    status = 'in_mainmenu'
    while True:
        print(f"\n+{'-' * 26}+")
        print(f"| 1. {'Lennä':<21} |")
        print(f"| 2. {'Vaihda kulkuvälinettä':<10} |")
        print(f"+{'-' * 26}+")
        todo = input("\nValitse mitä haluat tehdä: ").upper()
        if todo.isdigit():
            todo = int(todo)
            if todo == 1:
                return
            elif todo == 2:
                transport_valikko()
                return
            else:
                print("\nVain numerot (1 ja 2) ja help käyvät vastaukseksi.")
                continue
        elif todo == 'HELP':
            help(status)
            continue
        else:
            print("\nVain numerot (1 ja 2) ja help käyvät vastaukseksi.")
            continue


def calculate_distance(current_location, next_location):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{next_location}';"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    #lasketaan etäisyys nykyisen ja tulevan kentän välillä
    distance = (geodesic(current_location, result).km)
    if query_cursor.rowcount > 0:
        return distance


def welcome_screen():  # Pelin aloitusruutu
    run_intro = True   # Määrittää että intro on käynnissä
    username_selection = True  # Alustaa nimimerkin valintafunktion
    selected_username = []     # Lista johon tallennetaan käyttäjän asettama nimi
    while run_intro:
        print("X---X---X---X---X---X---X---X---X\n"
              "         Flying Bolivar!"
              "\nX---X---X---X---X---X---X---X---X\n")
        time.sleep(5)   # Ajastin joka rytmittää tekstin syötön
        print("Ilmatieteen laitoksen tietokantapalvelin on "
              "kaatunut, ja he tarvitsevat pikaisesti apuasi!"
              "\nTehtäväsi on tarkistaa tietokantapalvelimelta löytyvät sääolosuhteet\n")
        time.sleep(5)
        print("Sinun pitää saavuttaa 8 erilaista sääolosuhdetta "
              "lentämällä maailman eri lentokenttien välillä "
              "mahdollisimman nopeasti!")
        time.sleep(5)
        print("\nGreenPeace on saanut vihiä tehtävästäsi ja vaatii "
              "pitämään hiilidioksidin kulutuksesi mahdollisimman alhaisena.")
        time.sleep(2)
        print("Muuten kuulemma ampuvat kulkupelisi alas taivaalta...\n")
        time.sleep(2)
        print("Valttavanasi on 5 erilaista kulkupeliä, joita "
              "voit vaihtaa lentokenttien välillä:\n\n "
              "Luokka.           Nopeus.          Kulutus.\n"
              "\nLentokone         Keskitaso        Keskitaso.\n"
              "Helikopteri       Keskitaso        Keskitaso\n"
              "Hävittäjä         Suuri            Suuri\n"
              "Kuumailmapallo    Erittäin Hidas   Minimaalinen\n"
              "Liitokone         Hidas            Olematon\n\n")
        time.sleep(2)
        print("Saat aina apua pelin edetessä kirjoittamalla help!\n\n")
        time.sleep(5)
        understood = input("Kun olet ymmärtänyt tehtäväsi, paina enter-näppäintä.")
        if understood == "":    # Lopettaa introtekstin enterillä ja aloittaa käyttäjänimen pyynnin
            run_intro = False
            while username_selection:
                select_username = input("\nValitse käyttäjänimi (Max 10. merkkiä.):\n")
                if select_username == "":
                    print("Syötä käyttäjänimi!")
                elif len(select_username) > 10:   #jos käyttäjänimi on liian pitkä, pyydetään se uudestaan.
                    print("Liian pitkä käyttäjänimi!")
                else:
                    selected_username.append(select_username)
                    username_selection = False
    return selected_username


def scorecounter(time,remaining_budget):   # Laskee pisteet käytetyn ajan ja hiilidioksidibudjetin perusteella
    timescore = 999999 * (1 / time[1])
    if "iddqd" in playername:
        player['Score'] = (timescore + remaining_budget) * 5
    else:
        player['Score'] = timescore + (remaining_budget * 2)
    return


def travel_time(distance_traveled, aircraft_speed):         #Pelaajan lentoajan laskeminen
    time = distance_traveled[0] / aircraft_speed['speed']
    player['Travel_time'][0] = time
    player['Travel_time'][1] += time
    return


def co2_counter(distance_traveled, aircraft):  # Pelaajan käyttämän co2-budjetin laskuri
    distance_by_speed = distance_traveled[0] / aircraft['speed'] / 1000
    distance_by_consumption = distance_traveled[0] * aircraft['consumption'] / 1000
    player_budget = distance_by_speed + distance_by_consumption
    if "iddqd" in playername:
        player['CO2_budget'] += player_budget
    else:
        player['CO2_budget'] -= player_budget
    if player['CO2_budget'] < 0:
        player['CO2_budget'] = 0
        return
    else:
        return


# MAIN PROGRAM STARTS #

playername = welcome_screen()

player = {'Name' : playername, 'Current_location' : ['EU', 'FI', 'Helsinki-Vantaa', 'EFHK', (60.3172, 24.963301)],
          'Visited' : ['EFHK'], 'Transport' : '', 'Goals' : [], 'CO2_budget' : 10000, 'Score' : 0,
          'Distance' : [0, 0], 'Travel_time' : [0, 0]}

weather_goals = ("kuuma", "kylmä", "0-astetta", "10-astetta", "20-astetta", "kirkas", "pilvinen", "tuulinen") #säätila tavoitteet

transport_valikko()

while len(player['Goals']) < 8 and player['CO2_budget'] > 0:
    main_menu()
    continent = select_continent()
    country = select_country(continent)
    select_airport_n_fly(country)

if len(player['Goals']) == 8:
    scorecounter(player['Travel_time'], player['CO2_budget'])
    print(f"\nCONGRATS! SAAVUTIT KAIKKI SÄÄTILAT!")
    print(f"Sait {player['Score']:.0f} pistettä")
    print(f"Matkasi kokonaismatka oli {player['Distance'][1]:.0f}km")
    print(f"Matkasi kesto oli {player['Travel_time'][1]:.0f} tuntia")
    print(f"CO2-Budjettia jäi {player['CO2_budget']:.0f}")
    top10(player['Name'][0], player['Score'])
else:
    print(f"\nGAME OVER! CO2-Budjettisi ylittyi :(")

#LOL
