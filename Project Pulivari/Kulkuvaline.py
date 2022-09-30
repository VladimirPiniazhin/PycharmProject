

#def aircraft():
liitokone = {'name': 'Liitokone', 'speed': 60, 'consumption': 50}
lentokone = {'name': 'Lentokone', 'speed': 600, 'consumption': 120}
helikopteri = {'name': 'Helikopteri', 'speed': 300, 'consumption': 100}
havittaja = {'name': 'Havittaja', 'speed': 1200, 'consumption': 300}
kuumailmapallo = {'name': 'Kuumailmapallo', 'speed': 50, 'consumption': 10}

aircraft = (liitokone, lentokone, helikopteri, havittaja, kuumailmapallo)
    #return aircraft

k = aircraft[1]
#for key,value in lentokone.items():
    #print(key, ':', value)
print(k)
print(f"Valitsit: {k['name']} \nVauhti: {k['speed']} (km/h) \nKulutus: {k['consumption']}")
