import random
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

class Kilpailu:
    "Tämä luokka kuvailee kilpailun ominaisuksia"
    def __init__(self, kilpailu_nimi, reitin_pituus, autot):
        self.kilpailu_nimi = kilpailu_nimi
        self.reitin_pituus = reitin_pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):

        x = PrettyTable()

        x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]

        x.add_row(["Adelaide", 1295, 1158259, 600.5])
        x.add_row(["Brisbane", 5905, 1857594, 1146.4])
        x.add_row(["Darwin", 112, 120900, 1714.7])
        x.add_row(["Hobart", 1357, 205556, 619.5])
        x.add_row(["Sydney", 2058, 4336374, 1214.8])
        x.add_row(["Melbourne", 1566, 3806092, 646.9])
        x.add_row(["Perth", 5386, 1554769, 869.4])

    def kilpailu_ohi(self):
        i = True
        while i:
            self.tunti_kuluu()
            if self.autot.matka >= self.reitin_pituus:
                i = False
        return True

# PÄÄOHJELMA

autot = []

for i in range(10):
    n = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i+1}", n))

kisat = Kilpailu("Suuri romuralli", 8000, autot)

    while True:
        kisat.kilpailu_ohi()

kisat.tulosta_tilanne

#for auto in autot:
   # print("\n".join((f"Rekisteritunnus: {auto.rekkari:>20}", f"Huippunopeus: {auto.huippunopeus:>23}",
               #  f"Tämänhetkillinen nopeus: {auto.nopeus:>12}", f"Kuljettu matka: {auto.matka:>21}")))
print()