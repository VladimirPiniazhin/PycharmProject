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

# PÄÄOHJELMA

t = Talo(0,10,3)
#print(t.h_maara)
print(t.hissit[1].kerros)
t.aja_hissia(1, 3)
print(t.hissit[1].kerros)
t.aja_hissia(1, 6)
print(t.hissit[1].kerros)