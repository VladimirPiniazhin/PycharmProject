import random

def Heittely(n):
    n = 0
    i = 0
    while n != 6:
        n = random.randint(1, 6)
        i += 1
        if n != 6:
            print(f"{i+1}. nro: {n}")

    return print(f"{i+1}. nro: {n}")

Heittely(6)