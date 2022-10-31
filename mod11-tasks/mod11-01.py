#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
# alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
# julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:

    lukumaara = 0

    def __init__(self, nimi):
        self.nimi = nimi
        Julkaisu.lukumaara += 1
        self.lukumaara = Julkaisu.lukumaara


    def tulosta_tiedot(self):
        pass
        #print(f"{self.lukumaara}: {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("\n".join((f"Julkaisun tyypi:        Kirja", f"#: {self.lukumaara:>26}", f"Nimi: {self.nimi:>23}",
                 f"Kirjoittaja: {self.kirjoittaja:>16}", f"Sivumaara: {self.sivumaara:>18}")))
        print()

class Lehti(Julkaisu):

    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("\n".join((f"Julkaisun tyypi:        Lehti", f"#: {self.lukumaara:>26}", f"Nimi: {self.nimi:>23}",
                 f"Päätoimittaja: {self.paatoimittaja:>14}")))
        print()

# PÄÄOHJELMÄ

julkaisut = []

julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))


for t in julkaisut:
    t.tulosta_tiedot()