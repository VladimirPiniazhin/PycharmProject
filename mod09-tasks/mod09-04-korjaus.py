import random
class Auto:
    "Tämä luokka kuvailee auton ominaisuksia"

    nopeus = 0
    matka = 0

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus

    def kiihdyta(self, v):
        self.nopeus = self.nopeus + v
        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus <= 0:
            self.nopeus = 0

    def kulje(self, t):
        self.matka = self.matka + self.nopeus * t

# PÄÄOHJELMA

autot = []

for i in range(10):
    n = random.randint(100, 200)
    autot.append(Auto(f"ABC-{i+1}", n))

i = True

while i:
    for auto in autot:
        auto.kiihdyta(random.randint(-10, 15))
        auto.kulje(1)
        if auto.matka >= 10000:
            i = False


for auto in autot:
    print("\n".join((f"Rekisteritunnus: {auto.rekkari:>20}", f"Huippunopeus: {auto.huippunopeus:>23}",
                 f"Tämänhetkillinen nopeus: {auto.nopeus:>12}", f"Kuljettu matka: {auto.matka:>21}")))
    print()