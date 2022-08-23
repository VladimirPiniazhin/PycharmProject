import math
import random

#name = input("Nimesi:")
#fullname = input("Sukunimisi:")
#age = input("Mikä ikäinen sinä olet:")
#fullname = "Kontio"
#name = "Kalle"
#print("Morjes, ", name,"!")
#int value
#alennus = float(age) + 1
# float value
#wallet_balance = 15.40
# merkkijonojen liitäminen
#user = name +" " + fullname
#print("Käyttäjä "+ user + "on " + str(alennus) + " vuotta")
#print("Sullä on lompakossa " + str(wallet_balance) + " euroa" )
#ticket_price = input(user + " osti bussilipun, hinta?")
#wallet_balance = wallet_balance - float(ticket_price)
#print(f"Hänellä on lompakossa {wallet_balance} euroa")


#toinen esimerkki
#Ympyrän pinra-alan laskeminen
#Kaava Pii*r2
#Säde - "radius"
radius = input ("Anna ympyrän säde (m):")
area = math.pi*float(radius)*float(radius)
print(f"{radius} (m) säteisin ympyrän pinta-ala on {area:.3f} neliömetriä")


#Sattunaisluvun tuottaminen
rundom_number = random.randint(1,9)
print(f"Arvottu numero väliltä 1-9:{rundom_number}")