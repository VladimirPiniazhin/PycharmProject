
#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit
# siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko
# kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen
# siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    "Tämä luokka kuvailee hissin ominaisuksia"

    kerros = 0  #Nykyinen kerros
    def __init__(self, alimman, ylimman):
        self.alimman = alimman
        self.ylimman  = ylimman

    def siirry_kerrokseen(self, n):
        while self.kerros != n:
           if n > self.kerros:
               self.kerros_ylos()
               print(f"Nyt on {self.kerros}")
           elif n < self.kerros:
               self.kerros_alas()
               print(f"Nyt on {self.kerros}")
        print(f"Saapuneet {self.kerros}")
    def kerros_ylos (self):
       self.kerros += 1

    def kerros_alas(self):
       self.kerros -= 1

# PÄÄOHJELMA

h = Hissi(0, 5)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(3)
h.siirry_kerrokseen(0)
