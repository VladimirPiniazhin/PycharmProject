import requests
import json
#hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.chucknorris.io/jokes/random" #+ hakusana
vastaus = requests.get(pyynto).json()

#print(vastaus)
#print(json.dumps(vastaus, indent=2))

print(vastaus["value"])