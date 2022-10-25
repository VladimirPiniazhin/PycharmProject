#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja
# kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina
# saatuihin arvoihin. Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    "Tämä luokka kuvailee auton ominaisuksia"
    nopeus = 0
    kuljettu_matka = 0

    def __init__(self, rekkari, huippunopeus):
        self.rekkari = rekkari
        self.huippunopeus = huippunopeus


# PÄÄOHJELMA

auto1 = Auto("ABC-123", 142)
print(f"1.Auton ominaisuukset:")
print("\n".join((f"Rekisteritunnus: {auto1.rekkari:>20}", f"Huippunopeus: {auto1.huippunopeus:>23}",
                 f"Tämänhetkillinen nopeus: {auto1.nopeus:>12}", f"Kuljettu matka: {auto1.kuljettu_matka:>21}")))



