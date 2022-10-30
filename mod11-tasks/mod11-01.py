#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat
# alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tudostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa
# julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien
# julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:

    julkaisoiden_lukumaara = 0

    def __int__(self, nimi):
        Julkaisu.julkaisoiden_lukumaara += 1
        self.numero = Julkaisu.julkaisoiden_lukumaara
        self.nimi = nimi

    def tulosta_tiedot(self):
        pass

class Kirja(Julkaisu):

    def __int__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__int__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("\n".join((f"#: {self.numero:>20}", f"Nimi: {self.nimi:>23}",
                 f"Kirjoittaja: {self.kirjoittaja:>12}", f"Sivumaara: {self.sivumaara:>21}")))

class Lehti(Julkaisu):

    def __int__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__int__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print("\n".join((f"#: {self.numero:>20}", f"Nimi: {self.nimi:>23}",
                 f"Päätoimittaja: {self.paatoimittaja:>12}")))