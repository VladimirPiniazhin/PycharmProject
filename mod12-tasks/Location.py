from geopy.geocoders import Nominatim  # Kirjaston kytkentämien
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="Tester")  # Määritetään sovellus
address_1 = str(input('Введите город 1: \n'))  # 1. kaupungin määrittäminen
address_2 = str(input('Введите город 2: \n'))  # 2. kaupungin määrittäminen
location_1 = geolocator.geocode(address_1)  # Saadetaan 1. kaupungin koko nimi
location_2 = geolocator.geocode(address_2)  # Saadetaan 2. kaupungin koko nimi
print('1. Kaupunki: ', location_1)  # Tulostetaan tiedot
print('1. kaupungin koordinaatit: ', location_1.latitude, location_1.longitude)  # # Tulostetaan tiedot
gps_point_1 = location_1.latitude, location_1.longitude  # Tulostetaan 1. kaupungin koordinaatit
gps_point_2 = location_2.latitude, location_2.longitude  # Tulostetaan 2. kaupungin koordinaatit
print('2. kaupungin koordinaatit: ', location_2.latitude, location_2.longitude)  # # Tulostetaan tiedot
print('Etäisyys 1. kaupungilta', location_1, '2. kaupungille ', location_2, ': ',
      geodesic(gps_point_1, gps_point_2).kilometers, ' km')  # Tulostetaan tiedot