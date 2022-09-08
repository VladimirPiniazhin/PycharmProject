import random

tahkot = int(input("Anna nopan haluttun tahkojen määrä: "))

def heittely(tahkot):
    i = 0
    x = 0
    while x != tahkot:
        x = random.randint(1, tahkot)
        i += 1
        if x != tahkot:
            print(f"{i+1}. nro: {x}")

    return print(f"{i+1}. nro: {x}")

heittely(tahkot)