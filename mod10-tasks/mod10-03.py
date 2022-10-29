#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.
import time
class Hissi:
    "Tämä luokka kuvailee hissin ominaisuksia"

    #kerros = 0  #Nykyinen kerros
    def __init__(self, alimman, ylimman):
        self.alimman = alimman
        self.ylimman  = ylimman
        self.kerros = 0  # Nykyinen kerros

    def siirry_kerrokseen(self, n):
        if n < self.alimman or n > self.ylimman:
            return
        while self.kerros != n:
           if n > self.kerros:
               self.kerros_ylos()
               time.sleep(1)
               print(f"Nyt on {self.kerros}. kerros")
           elif n < self.kerros:
               self.kerros_alas()
               time.sleep(1)
               print(f"Nyt on {self.kerros}. kerros")
        #print(f"Olemme saapuneet. {self.kerros}. kerros")
        time.sleep(1)

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
        self.num = num
        print(f"Hissi nro {num+1} lähtee {n}. kerrokseen")
        self.hissit[num - 1].siirry_kerrokseen(n)
        print(f"Hissi nro {num+1} on {n}. kerroksessa")

    def palohalytys(self):
        print(f"Huomio! Tulipalo!")
        time.sleep(1)
        for i in range(1, self.h_maara+1):
            self.aja_hissia(i - 1, 0)

# PÄÄOHJELMA

t = Talo(0,10,3)

t.aja_hissia(1, 7)

time.sleep(1)

t.palohalytys()







