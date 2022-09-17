# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen

import random
list_n = []
n = " "

while n != "":
    n = input("Syötä nimi: ")
    if n in list_n:
        print("Aiemmin syötetty nimi")
    elif n == "":
        print("Ohjelma lopetettu")
    else:
        print("Uusi nimi")
        list_n.append(n)

new_list = list(list_n)
random.shuffle(new_list)

for i in new_list:
    print(i)