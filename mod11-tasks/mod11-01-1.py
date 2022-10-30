#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
# alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
# julkaisujen kaikki tiedot toteuttamiesi metodien avulla.
class Julkaisu:
    "Tämä luokka kuvailee auton ominaisuksia"

    lukumaara = 0

    def __init__(self, nimi):
        self.nimi = nimi
        Julkaisu.lukumaara += 1
        self.lukumaara = Julkaisu.lukumaara

    def tulosta(self):
        pass

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, s_maara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.s_maara = s_maara

    def tulosta(self):
        super().tulosta()
        print("\n".join((f"Julakisu #: {self.lukumaara}", f"Type: Kirja", f"Nimi: {self.nimi}", f"Kirjoittaja: {self.kirjoittaja}", f"Sivumäärä: {self.s_maara}")))

class Lehti(Julkaisu):

    def __init__(self, nimi, paatomittaja):
        super().__init__(nimi)
        self.paatomittaja = paatomittaja

    def tulosta(self):
        super().tulosta()
        print("\n".join((f"Julakisu #: {self.lukumaara}", f"Type: Lehti",  f"Nimi: {self.nimi}", f"Päätoimittaja: {self.paatomittaja}")))

# PÄÄOHJELMA

julkaisut = []


julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))

for t in julkaisut:
    t.tulosta()
    print()






