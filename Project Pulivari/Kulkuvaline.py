
def aircraft_valiko(n):
    liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50}
    lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 120}
    helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 100}
    havittaja = {'name': 'Hävittäjä', 'speed': 1200, 'consumption': 300}
    kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}
    transport = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)
    k = transport[n]
    print(f"Valitsit: {k['name']} \nVauhti: {k['speed']} (km/h) \nKulutus: {k['consumption']} (CO2)")
    return k


