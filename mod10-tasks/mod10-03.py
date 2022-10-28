#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
import time


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

    def palohalytys(self):
        self.hissit.siirry_kerrokseen(0)

# PÄÄOHJELMA

t = Talo(0,10,3)

t.aja_hissia(1, 7)
print(f"Olet {t.hissit[1].kerros}. kerroksessa")

time.sleep(3)

t.palohalytys()

print(f"Olet {t.hissit[1].kerros}. kerroksessa")




