
def aircraft_valiko(n):
    liitokone = {'name': 'liitokone', 'speed': 60, 'consumption': 50}
    lentokone = {'name': 'lentokone', 'speed': 600, 'consumption': 120}
    helikopteri = {'name': 'helikopteri', 'speed': 300, 'consumption': 100}
    havittaja = {'name': 'havittaja', 'speed': 1200, 'consumption': 300}
    kuumailmapallo = {'name': 'kuumailmapallo', 'speed': 50, 'consumption': 10}
    aircraft_list = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)
    # aircraft_list = k()
    k = aircraft_list[n]
    print(f"valitsit: {k['name']} \nvauhti: {k['speed']} (km/h) \nkulutus: {k['consumption']}")
    return k

aircraft = aircraft_valiko(0)
# aircraft_list = aircraft()
# for key,value in lentokone.items():
# print(key, ':', value)
# k = aircraft_list[1]
#print(f"valitsit: {aircraft['name']} \nvauhti: {aircraft['speed']} (km/h) \nkulutus: {aircraft['consumption']}")
