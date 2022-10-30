#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on
# ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden
# ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman
# kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden
# polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja
# ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

from prettytable import PrettyTable

class Auto:
    "Tämä luokka kuvailee auton ominaisuksia"

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, v):
        self.nopeus = self.nopeus + v
        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus <= 0:
            self.nopeus = 0

    def kulje(self, t):
        self.matka = self.matka + self.nopeus * t

class Sahkoauto(Auto):

    def __init__(self, rekkari, huippunopeus, akkukapasiteetti):
        super().__init__(rekkari, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):

    def __init__(self, rekkari, huippunopeus, bensatankki):
        super().__init__(rekkari, huippunopeus)
        self.bensatankki = bensatankki

# PÄÄOHJELMA

autot = []

def tulosta():
    x = PrettyTable()

    x.field_names = ["Rekkari", "Huippunopeus", "Tämänhetkillinen nopeus", "AKuljettu matka"]

    x.add_row([autot[0].rekkari, autot[0].huippunopeus, autot[0].nopeus, autot[0].matka])
    x.add_row([autot[1].rekkari, autot[1].huippunopeus, autot[1].nopeus, autot[1].matka])

    print(x)

autot.append(Sahkoauto("ABC-15", 180, 52.5))
autot.append(Polttomoottoriauto("ACD-123", 165, 32.3))

autot[0].kiihdyta(112)
autot[1].kiihdyta(120)

for auto in autot:
    auto.kulje(3)
tulosta()






