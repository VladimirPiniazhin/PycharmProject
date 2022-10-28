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
        if n < self.alimman or n > self.ylimman:
            return
        while self.kerros != n:
           if n > self.kerros:
               self.kerros_ylos()
               print(f"Nyt on {self.kerros} kerros")
           elif n < self.kerros:
               self.kerros_alas()
               print(f"Nyt on {self.kerros} kerros")
        print(f"Olemme saapuneet {self.kerros}")

    def kerros_ylos (self):
       self.kerros = self.kerros + 1

    def kerros_alas(self):
       self.kerros = self.kerros - 1


class Talo:
    "Tämä luokka kuvailee talon ominaisuksia"

    def __init__(self, alimman, ylimman, h_maara):
        self.h_maara = h_maara
        self.hissit = []
        for i in range(self.h_maara):
            self.hissit.append(Hissi(alimman, ylimman))

    def aja_hissia(self, num, n):
        self.hissit[num].siirry_kerrokseen(n)

# PÄÄOHJELMA

t = Talo(0,10,3)
#print(t.h_maara)
print(t.hissit[1].kerros)
t.aja_hissia(1, 3)
print(f"Olet {t.hissit[1].kerros}. kerroksessa")
