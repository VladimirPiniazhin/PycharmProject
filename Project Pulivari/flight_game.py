import random
import mysql.connector

connection = mysql.connector.connect( # Täytyy vaihtaa username ja password kun testaa koodin toimivuutta.
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Yahoo',
    autocommit=True
)


def db_distinct_from_table(column): # Haetaan taulusta kaikki yhden sarakkeen eri arvot. Käytetään listaamaan maanosat.
    sql = f"SELECT DISTINCT {column} FROM country"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result


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
    sql = f"SELECT airport.name, airport.ident FROM airport, country WHERE country.iso_country = airport.iso_country " \
          f"and airport.iso_country = '{country}' and airport.type in ({airport_type})"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result

def db_airport_name_ident_xy_by_ident(ident): # Valitaan airport tauluta nimi, ident, koordinaatit ident-koodin perusteella
    sql = f"SELECT name, ident, latitude_deg, longitude_deg FROM airport WHERE ident = '{ident}'"
    query_cursor = connection.cursor()
    query_cursor.execute(sql)
    result = query_cursor.fetchall()
    return result


def select_continent(): # Valitaan maanosa
    continents = db_distinct_from_table('continent') # Kutsutaan functio parametrina 'continent'
    continent_list = ("EU", "AS", "NA", "AF", "AN", "SA", "OC") # Listasta ei saada maanosan nimiä, joudutaan
                                                                # toteuttamaan listaus toisin.
    while True:
        print(f"\n+{'-' * 24}+")
        print(f"| {continents[0][0]:<2} : {'Eurooppa':<17} |")
        print(f"| {continents[1][0]:<2} : {'Aasia':<17} |")
        print(f"| {continents[2][0]:<2} : {'Pohjois-Amerikka':<17} |")
        print(f"| {continents[3][0]:<2} : {'Afrikka':<17} |")
        print(f"| {continents[4][0]:<2} : {'Etelämanner':<17} |")
        print(f"| {continents[5][0]:<2} : {'Etelä-Amerikka':<17} |")
        print(f"| {continents[6][0]:<2} : {'Oseania':<17} |")
        print(f"+{'-' * 24}+\n")
        continent_selection = input("Valitse maanosa: ").upper()
        if continent_selection.isalpha() and continent_selection in continent_list:
            player_location[0] = continent_selection # Päivitetään pelaajan sijainti
            return
        else:
            print("\nMaanosaa ei löydy.\n")
            continue


def select_country(): # Valitaan maan
    while True:
        countries_list = []
        countries = db_iso_country_name_by_continent(player['Current_location'][0]) # Kutsutaan fuction pelaajan
                                                                                    # nykyisen sijainnin maanosan
                                                                                    # perusteella
        print(f"\n+{'-' * 45}+")
        for i in countries:
            print(f"|  {i[0]:<5}  {i[1]:<35} |")
            countries_list.append(i[0]) # Lisätään listaan ISO_country koodi
                                        # jotta voidaan tarkistaa onko inputti listassa
        print(f"+{'-' * 45}+\n")
        country_selection = input("Valitse maa: ").upper()
        if country_selection in countries_list:
            player_location[1] = country_selection # Päivitetään pelaajan sijainta.
            return
        else:
            print("\nMaata ei löydy.")
            continue


def select_airport(): # Valitaan lentokenttä listasta
    while True:
        airport_type = airport_type_by_transport(player['Transport']) # Määritetään lentokentän tyyppi pelaajan
                                                                      # nykyisen menopelin perusteella
        airport = db_airport_by_country_transport(player['Current_location'][1], airport_type)  # Haetaan lentokentät
                                                                                                # nykyisen sijainnin ja
                                                                                                # lentokentän tyypin
                                                                                                # perusteella
        if len(airport) > 0:
            airport_list = []
            print(f"\n+{'-' * 59}+")
            for i in airport:
                print(f"| {i[0]:<45}  {i[1]:>10} |")
                airport_list.append(i[1]) # Lisätään lentokentän ident listaan tarkistaakseen input.
            print(f"+{'-' * 59}+\n")
            airport_selection = input("Valitse lentokenttä: ").upper()
            weather = random.choice(random_continent_weather()) # Kutsutaan säätila. rivi 144.
            if airport_selection in airport_list and weather not in player_goals and airport_selection not in visited_locations:
                airport = db_airport_name_ident_xy_by_ident(airport_selection) # Haetaan lentokentän tiedot identin perusteella.
                player_location[2] = airport[0][0]  #
                player_location[3] = airport[0][1]  # Päivitetään pelaajan sijainti.
                player_location[4] = airport[0][2]  #
                player_location[5] = airport[0][3]  #
                player_goals.append(weather) # Lisätään säätila pelaajan saavutus listaan.
                return
            elif airport_selection in visited_locations:
                print(f"\nOlet jo käynyt täällä tai sää on sama kuin saavuttamasi.")
            elif weather in player_goals:
                print(f"\nSää lentokentällä {weather}. Olit saavuttanut jo kyseisen säätilan. Valitse uusi lentokenttä.")
                visited_locations.append(airport_selection)
                continue
            else:
                print("\nLentokenttää ei löydy.")
                continue
        else:
            print(f"\nLentokenttää ei löytynyt {player['Transport']}:lle.")
            break


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
        airport_type = "'balloonport'"
        return airport_type
    elif transport == "Helikopteri":
        airport_type = "'heliport'"
        return airport_type


def random_continent_weather():     # Säätila määritellään pelaajan sen hetkisen sijainnin maanosan perusteella
                                    # tehdään vasta kun lentokenttä on valittu
    if 'EU' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [1, 2, 2, 2, 1, 1, 2, 2], k = 13)
        return continent_weather
    elif 'AS' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [10, 1, 1, 3, 5, 8, 6, 3], k = 36)
        return continent_weather
    elif 'NA' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [2, 5, 5, 5, 3, 5, 5, 8], k = 38)
        return continent_weather
    elif 'AF' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [10, 1, 1, 4, 5, 1, 5, 5], k = 32)
        return continent_weather
    elif 'AN' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [20, 1, 1, 1, 1, 3, 2, 2], k = 31)
        return continent_weather
    elif 'SA' in player['Current_location']:
        continent_weather = random.choices(weather_goals, weights = [10, 1, 1, 2, 1, 1, 2, 2], k = 21)
        return continent_weather
    else: #OC
        continent_weather = random.choices(weather_goals, weights = [9, 1, 2, 2, 3, 3, 3, 2], k = 25)
        return continent_weather


# MAIN PROGRAM STARTS #

player_goals = []   # Listaan lisätään aina alkio kun saavutetaan uusi päämäärä.
visited_locations = ['EFHK']    # Listaan lisätään aina alkio kun on käyty lentokentällä tai säätila on sama.
player_location = ['EU', 'FI', 'Helsinki-Vantaa', 'EFHK', 0, 0] # Nykyinen sijainti (viimeiset luvut on koordinaatit. HKI?)
transports = ['Hävittäjä', 'Helikopteri', 'Lentokone', 'Kuumailmapallo', 'Liitokone'] #Tämä pitää saada kirjastoksi
                                                                                      # jossa myös kulkuvälineellä nopeus
                                                                                        # ja co2-kerroin)
player = {'Current_location' : player_location, 'Transport' : transports[0]} # pelaajan tiedot, pitää lisätä vielä nimi
                                                                             # ja c02 budjetti ainaskin
weather_goals = ("hot", "cold", "0deg", "10deg", "20deg", "clear", "clouds", "windy") #säätila tavoitteet

for i in range(3): # Testataan peliä kolmella rundilla. Puuttuu menu, kulkuvälineen valinta, help ja laskenta functiot
    select_continent()
    select_country()
    select_airport()
    print(f"\nNykyinen sijaintisi: {player['Current_location']}")
    print(f"\nSaavuttamasi säätilat: {player_goals}")