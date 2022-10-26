#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi. Jatka pääohjelmaa siten,
# että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse
# vielä päivittää.

class Auto:
    "Tämä luokka kuvailee auton ominaisuksia"

    nopeus = 0
    kuljettu_matka = 0

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus

    def kiihdyta(self, v):
        self.nopeus = self.nopeus + v
        if self.nopeus >= self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus <= 0:
            self.nopeus = 0

# PÄÄOHJELMA

auto1 = Auto("ABC-123", 142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"1.Auton ominaisuukset:")
print("\n".join((f"Rekisteritunnus: {auto1.rekkari:>20}", f"Huippunopeus: {auto1.huippunopeus:>23}",
                 f"Tämänhetkillinen nopeus: {auto1.nopeus:>12}", f"Kuljettu matka: {auto1.kuljettu_matka:>21}")))

print()

auto1.kiihdyta(-200)


print(f"1.Auton ominaisuukset:")
print("\n".join((f"Rekisteritunnus: {auto1.rekkari:>20}", f"Huippunopeus: {auto1.huippunopeus:>23}",
                 f"Tämänhetkillinen nopeus: {auto1.nopeus:>12}", f"Kuljettu matka: {auto1.kuljettu_matka:>21}")))

