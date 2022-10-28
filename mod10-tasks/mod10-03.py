#Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki
# hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.


class Hissi:
    "Tämä luokka kuvailee hissin ominaisuksia"

    kerros = 0  #Nykyinen kerros
    def __init__(self, alimman, ylimman):
        self.alimman = alimman
        self.ylimman  = ylimman

    @classmethod

    def siirry_kerrokseen(cls, n):
        while cls.kerros != n:
           if n > cls.kerros:
               cls.kerros_ylos()
               print(f"Nyt on {cls.kerros}")
           elif n < cls.kerros:
               cls.kerros_alas()
               print(f"Nyt on {cls.kerros}")
        print(f"Saapuneet {cls.kerros}")
    def kerros_ylos (cls):
       cls.kerros = cls.kerros + 1

    def kerros_alas(cls):
       cls.kerros = cls.kerros - 1


class Talo:
    "Tämä luokka kuvailee hissin ominaisuksia"

    kerros = 0  #Nykyinen kerros
    hissit = []

    def __init__(self, alimman, ylimman, h_maara):
        super().__init__(alimman, ylimman)
        self.h_maara = h_maara

        for i in range(self.h_maara):
            self.hissit.append(Hissi)

    def aja_hissia(self, num, n):
        while self.hissit[num].kerros != n:
            if n > self.hissit[num].kerros:
                #self.hissit[num].kerros_ylos(self)
                self.hissit[num].kerros += 1
                print(f"Nyt on {self.hissit[num].kerros}")
            elif n < self.hissit[num].kerros:
                #self.hissit[num].kerros_alas(self)
                self.hissit[num].kerros -= 1
                print(f"Nyt on {self.hissit[num].kerros}")
        print(f"Saapuneet {self.hissit[num].kerros}")

    def palohalytys(self):
        for hissi in self.hissit:
            hissi = list(map(Hissi.siirry_kerrokseen(0), self.hissit))

# PÄÄOHJELMA

t = Talo(0,10,3)
#print(t.h_maara)
print(t.hissit[1].kerros)
t.aja_hissia(1, 3)
print(t.hissit[1].kerros)
t.aja_hissia(1, 6)
print(t.hissit[1].kerros)