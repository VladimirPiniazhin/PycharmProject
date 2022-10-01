
def aircraft_valiko(n):
    liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50}
    lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 120}
    helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 100}
    havittaja = {'name': 'Havittaja', 'speed': 1200, 'consumption': 300}
    kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}
    aircraft_list = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)
    k = aircraft_list[n]
    print(f"Valitsit: {k['name']} \nVauhti: {k['speed']} (km/h) \nKulutus: {k['consumption']} (CO2)")
    return k


