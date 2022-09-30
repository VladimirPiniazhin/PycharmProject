

def aircraft_valiko(n):
    liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50}
    lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 120}
    helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 100}
    havittaja = {'name': 'Havittaja', 'speed': 1200, 'consumption': 300}
    kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}
    aircraft_list = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)
    #aircraft_list = k()
    k = aircraft_list[n]
    return k

aircraft = aircraft_valiko(0)
#aircraft_list = aircraft()
#for key,value in lentokone.items():
    #print(key, ':', value)
#k = aircraft_list[1]
print(f"Valitsit: {aircraft['name']} \nVauhti: {aircraft['speed']} (km/h) \nKulutus: {aircraft['consumption']}")
