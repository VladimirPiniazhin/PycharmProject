import random
import time
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
        for auto in self.autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)

    def kilpailu_ohi(self):
        for auto in autot:
            if auto.matka >= self.reitin_pituus:
                return True

    def tulosta_tilanne(self):

        x = PrettyTable()

        x.field_names = ["Rekkari", "Huippunopeus (km/h)", "Tämänhetkillinen nopeus (km/h)", "AKuljettu matka (km)"]

        x.add_row([self.autot[0].rekkari, self.autot[0].huippunopeus, self.autot[0].nopeus, self.autot[0].matka])
        x.add_row([self.autot[1].rekkari, self.autot[1].huippunopeus, self.autot[1].nopeus, self.autot[1].matka])
        x.add_row([self.autot[2].rekkari, self.autot[2].huippunopeus, self.autot[2].nopeus, self.autot[2].matka])
        x.add_row([self.autot[3].rekkari, self.autot[3].huippunopeus, self.autot[3].nopeus, self.autot[3].matka])
        x.add_row([self.autot[4].rekkari, self.autot[4].huippunopeus, self.autot[4].nopeus, self.autot[4].matka])
        x.add_row([self.autot[5].rekkari, self.autot[5].huippunopeus, self.autot[5].nopeus, self.autot[5].matka])
        x.add_row([self.autot[6].rekkari, self.autot[6].huippunopeus, self.autot[6].nopeus, self.autot[6].matka])
        x.add_row([self.autot[7].rekkari, self.autot[7].huippunopeus, self.autot[7].nopeus, self.autot[7].matka])
        x.add_row([self.autot[8].rekkari, self.autot[8].huippunopeus, self.autot[8].nopeus, self.autot[8].matka])
        x.add_row([self.autot[9].rekkari, self.autot[9].huippunopeus, self.autot[9].nopeus, self.autot[9].matka])

        print(x)

# PÄÄOHJELMA

autot = []

for i in range(10):
    n = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i+1}", n))

kisat = Kilpailu("Suuri romuralli", 8000, autot)

while kisat.kilpailu_ohi() != True:
    kisat.tunti_kuluu()
kisat.tulosta_tilanne()

