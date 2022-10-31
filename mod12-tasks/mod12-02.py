#Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api. Kirjoita ohjelma, joka kysyy käyttäjältä
# paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi. Palveluun rekisteröityminen on tarpeen, jotta saat
# rajapintapyynnöissä tarvittavan API-avaimen (API key). Selvitä myös, miten saat Kelvin-asteet
# muunnettua Celsius-asteiksi.
from prettytable import PrettyTable
import requests
import json
from geopy.geocoders import Nominatim  # Kirjaston kytkentämien

geolocator = Nominatim(user_agent="Tester")  # Määritetään sovellus
address = str(input("Syötä paikan (kaupungin) nimi: \n"))  # kaupungin määrittäminen
location = geolocator.geocode(address)  # Saadetaan kaupungin koko nimi
print("Kaupunki: ", location)  # Tulostetaan tiedot
print("kaupungin koordinaatit: ", location.latitude, location.longitude)  # Tulostetaan tiedot
gps_point = location.latitude, location.longitude  # Tulostetaan kaupungin koordinaatit

# Pyynnön malli:pyynto = f"http://api.openweathermap.org/geo/1.0/direct?q={kaupunki}&limit=1&appid=4d512b69b0f3cf24a7b6626699ed76bb" #+ hakusana

def tulosta():
    x = PrettyTable()
    x.field_names = ["Sky", "Temp (C)", "Pressure (mm)", "Wind speed (m/s)"]
    x.add_row([vastaus2["weather"][0]["main"], round((vastaus2["main"]["temp"]-273), 2), vastaus2["main"]["pressure"], vastaus2["wind"]["speed"]])
    print(x)

lat = location.latitude
lon = location.longitude

#print(lat)
#print(lon)

pyynto2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=4d512b69b0f3cf24a7b6626699ed76bb"
vastaus2 = requests.get(pyynto2).json()
#print(vastaus2)
#print(json.dumps(vastaus2, indent=2))

tulosta()

