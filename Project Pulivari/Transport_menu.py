
"""Kulkuvälineen valikko"""
def aircrafts(n):
    liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50}
    lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 120}
    helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 100}
    havittaja = {'name': 'Hävittäjä', 'speed': 1200, 'consumption': 300}
    kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}
    aircraft_list = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)
    transport = aircraft_list[n]
    print(f"Valitsit: {transport['name']} \nVauhti: {transport['speed']} (km/h) \nKulutus: {transport['consumption']} (CO2)")
    return transport

"""Kulkuvälineen valikko"""

def transport_valikko():
    print(f"Nykyinen sijaintisi: Helsinki-Vantaa\nValitse kulkuväline")
    print("1 - Liitokone \n2 - Lentokone \n3 - Helikopteri \n4 - Hävittäjä \n5 - Kuumailmapallo")

    n = int(input("Syötä kulkuvälineen numero: "))
    while n >= 6 or n <= 0:
        if n not in range(1,6):
            print("Virheellinen numero. Syötä numero uudelleen")
            n = int(input("Syötä kulkuvälineen numero: "))

    print("Great!")
    return n

n = transport_valikko()

aircrafts(n-1)