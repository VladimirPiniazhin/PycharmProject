
#Kulkuvälineen valikko

def aircrafts(n):

    #määritellään kulkuvälineet ja niiden ominaisuuksia

    liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50}
    lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 120}
    helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 100}
    havittaja = {'name': 'Hävittäjä', 'speed': 1200, 'consumption': 300}
    kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}

    #Lisätään ne listaan jota käyttää sitten niiden indexia

    aircraft_list = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)

    #Lisätään listan muuttujaan

    transport = aircraft_list[n]
    print(f"Valitsit: {transport['name']} \nVauhti: {transport['speed']} (km/h) \nKulutus: {transport['consumption']} (CO2)")
    return transport

 #Kulkuvälineen valikko

def transport_valikko():

    #Tulostetaan kulkuvälineen valikko

    print(f"Nykyinen sijaintisi: Helsinki-Vantaa\nValitse kulkuväline")
    print("1 - Liitokone \n2 - Lentokone \n3 - Helikopteri \n4 - Hävittäjä \n5 - Kuumailmapallo")

    #Kysytään kulkuvälineen valinta

    n = int(input("Syötä kulkuvälineen numero: "))

    #Tarkistetaan jota valinta oli oikein eli 1 ja 5 välillä

    while n >= 6 or n <= 0:
        if n not in range(1,6):
            print("Virheellinen numero. Syötä numero uudelleen")
            n = int(input("Syötä kulkuvälineen numero: "))

    print("Great!")

    #Palautetaan käyttäjän valinta (numero)

    return n

#Käytetään käyttäjän valinta (numero) kuin listan indeksi kun kutsutaan kulkuvälineen listasta

n = transport_valikko()

#Kutsutaan funktiosta kulkuväline. Koska listan indeksit ja kulkuvälineen valikko alkaa eri numeroilla, kullekin muuttujalle lisätään 1 jotta
    #saada sitten vastavia tuloksia

aircrafts(n-1)