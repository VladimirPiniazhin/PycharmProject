import random

silmaluku = input("Anna haluttu silmäluku: ")

def create_lottery_row(silmaluku):

    i = 0
    while silmaluku != 6:
        silmaluku = random.randint(1, 6)
        i += 1
        if silmaluku != 6:
            print(f"{i+1}. nro: {silmaluku}")

    return print(f"{i+1}. nro: {silmaluku}")

create_lottery_row(silmaluku)