import random
class Auto:
    "Tämä luokka kuvailee auton ominaisuksia"

    nopeus = 0
    matka = 0

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus
        self.autot = []

    def autoLisays(self, auto):
        self.autot.append(auto)

    def kiihdyta(self, v):
        self.nopeus = self.nopeus + v
        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus <= 0:
            self.nopeus = 0

    def kulje(self, t):
        self.matka = self.nopeus * t

# PÄÄOHJELMA



autot = [Auto(f"ABC-{i+1}", random.randint(100, 200)) for i in range(10)]

#for i in range(10):
    #auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    #autojen_list.append(auto)

print(autot)