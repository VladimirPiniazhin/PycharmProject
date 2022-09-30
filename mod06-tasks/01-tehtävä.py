import random

def Heittely():
    n = 0
    i = 0
    while n != 6:
        n = random.randint(1, 6)
        i += 1
        if n != 6:
            print(f"{i}. nro: {n}")

    return print(f"{i}. nro: {n}")

Heittely()