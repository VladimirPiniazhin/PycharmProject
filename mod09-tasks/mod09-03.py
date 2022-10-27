#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
# kasvattaa kuljetun matkan lukemaan 2090 km.


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
        self.matka = self.nopeus * t

# PÄÄOHJELMA

auto1 = Auto("ABC-123", 142)
auto1.kiihdyta(60)
auto1.kulje(2)


print(f"1.Auton ominaisuukset:")
print("\n".join((f"Rekisteritunnus: {auto1.rekkari:>20}", f"Huippunopeus: {auto1.huippunopeus:>23}",
                 f"Tämänhetkillinen nopeus: {auto1.nopeus:>12}", f"Kuljettu matka: {auto1.matka:>21}")))


