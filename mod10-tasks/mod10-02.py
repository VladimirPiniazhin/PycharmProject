#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
# ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin
# numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.
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
       self.kerros = self.kerros + 1

    def kerros_alas(self):
       self.kerros = self.kerros - 1


class Talo:
    "Tämä luokka kuvailee hissin ominaisuksia"

    kerros = 0  #Nykyinen kerros
    hissit = []
    def __init__(self, alimman, ylimman, h_maara):
        self.alimman = alimman
        self.ylimman  = ylimman
        self.h_maara = h_maara

        for i in range(self.h_maara):
            self.hissit.append(Hissi)
    def aja_hissia(self, num, n):
        #for self.hissit[num] in self.hissit:

# PÄÄOHJELMA

t = Talo(0,10,3)

print(t.hissit[1].kerros)
