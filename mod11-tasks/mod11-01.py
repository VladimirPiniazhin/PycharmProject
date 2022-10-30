#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
# alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
# julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:

    lukumaara = 0

    def __int__(self, nimi):
        self.nimi = nimi
        Julkaisu.lukumaara += 1
        self.lukumaara = Julkaisu.lukumaara


    def tulosta_tiedot(self):
        print(f"{self.lukumaara}: {self.nimi}")

class Kirja(Julkaisu):

    def __int__(self, nimi, kirjoittaja, sivumaara):
        super().__int__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("\n".join((f"#: {self.lukumaara:>20}", f"Nimi: {self.nimi:>23}",
                 f"Kirjoittaja: {self.kirjoittaja:>12}", f"Sivumaara: {self.sivumaara:>21}")))

class Lehti(Julkaisu):

    def __int__(self, nimi, paatoimittaja):
        super().__int__(nimi)
        self.paatoimittaja = paatoimittaja


    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("\n".join((f"#: {self.lukumaara:>20}", f"Nimi: {self.nimi:>23}",
                 f"Päätoimittaja: {self.paatoimittaja:>12}")))

# PÄÄOHJELMÄ

julkaisut = []

julkaisut.append(Kirja("Hytti n:o 6", "Rosa Liksom", 200))
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))


for t in julkaisut:
    t.tulosta_tiedot()