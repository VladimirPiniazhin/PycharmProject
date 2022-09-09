
import random
def list_summa(list):
    b = []
    for n in list:
        if n % 2 != 0:
            b.append(n)
    return b

a = []
numero = int(input("Syötä montako numeroa pitää olla listassa: "))
for i in range(numero):
    n = random.randint(1, 9999)
    a.append(n)

list_summa(a)

print(a)
print(list_summa(a))