#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä
# paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet
# muunnettua Celsius-asteiksi.

import requests
import json
from geopy.geocoders import Nominatim  # Подключаем библиотеку
from geopy.distance import geodesic  # И дополнения

geolocator = Nominatim(user_agent="Tester")  # Указываем название приложения
address_1 = str(input('Введите город 1: \n'))  # Получаем название первого города
location_1 = geolocator.geocode(address_1)  # Получаем полное название первого города
print('Город 1: ', location_1)  # Выводим первичные данные
print('Координаты города 1: ', location_1.latitude, location_1.longitude)  # Выводим координаты первого города
gps_point_1 = location_1.latitude, location_1.longitude  # Выводим координаты первого города






#kaupunki = input("Anna hakusana: ")
#api_key = "4d512b69b0f3cf24a7b6626699ed76bb"4d512b69b0f3cf24a7b6626699ed76bb

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto1 = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=1&appid=4d512b69b0f3cf24a7b6626699ed76bb" #+ hakusana

vastaus1 = requests.get(pyynto1).json()
#print(json.dumps(vastaus1, indent=2))

lat = vastaus1[0]["lat"]
lon = vastaus1[0]["lon"]

pyynto2 = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely, hourly, daily, alerts&appid=4d512b69b0f3cf24a7b6626699ed76bb"
vastaus2 = requests.get(pyynto2).json()
print(json.dumps(vastaus2, indent=2))